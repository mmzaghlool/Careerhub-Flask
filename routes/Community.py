from flask import Flask, request, jsonify
from flask.views import MethodView
from firebase_admin import auth, db
import json
import requests
from . import routes
from profanityfilter import ProfanityFilter

pf = ProfanityFilter()
pf.define_words(["fff", "sss", "shit", "fuck"])

class Community(MethodView):
    def get(self, comID, postID=None):
        try:

            # Get community posts
            if postID == None:
                # community = db.reference(path='community').order_by_child(
                #     'communityID').equal_to(comID).get()
                print(comID)

                url = 'http://18.222.72.221:9200/posts/post/_search'
                obj = {
                    "sort": [
                        {
                            "timeStamp": {
                                "order": "desc"
                            }
                        },
                        "_score"
                    ],
                    "query": {
                        "match": {
                            "communityID": comID
                        }
                    }
                }

                headers = {"Content-Type": "application/json"}
                x = requests.get(url, data=json.dumps(obj), headers=headers)
                print(x.text)

                return {
                    "success": True,
                    "message": "posts of your community",
                    "data": x.text
                }, 200

            # get specific post
            else:
                post = db.reference(path='community/{0}'.format(postID)).get()

                return {
                    "success": True,
                    "message": "posts of your community",
                    "data": post
                }, 200

        except Exception as f:
            return {
                "success": False,
                "message": "{0}".format(f)
            }, 400

    # add new post
    def post(self, comID):
        try:
            uid = request.json.get('uid')
            text = request.json.get('text')
            timeStamp = request.json.get('timeStamp')
            images = request.json.get('images')
            text = pf.censor(text)

            if((uid == None) | (text == None) | (timeStamp == None)):
                return {
                    "success": False,
                    "message": "Missing data"
                }

            else:
                imagesDict = {}
                if images is not None:
                    imagesDict = {i: images[i] for i in range(len(images))}

                print(imagesDict)
                print(images)
                user = db.reference(path='/users/{0}'.format(uid)).get()
                obj = {
                    "text": text,
                    "images": imagesDict,
                    "timeStamp": timeStamp,
                    "name": "{0} {1}".format(user["firstName"], user["lastName"]),
                    "avatar": user["avatar"],
                    "uid": uid,
                    "communityID": comID,
                }
                key = db.reference(path='community').push(obj).key

                url = 'http://18.222.72.221:9200/posts/post/{0}'.format(key)
                obj["key"] = key
                obj["likes"] = 0

                headers = {"Content-Type": "application/json"}
                x = requests.put(url, data=json.dumps(obj), headers=headers)

                print(x.text)
                return {
                    "success": True,
                    "message": "Post added"
                }

        except Exception as f:
            return {
                "success": False,
                "message": "{0}".format(f)
            }, 400

    # delete post
    def delete(self, typo=None, postID=None):
        try:
            db.reference(path='community/{0}'.format(postID)).delete()

            url = 'http://18.222.72.221:9200/posts/post/{0}'.format(postID)
            headers = {"Content-Type": "application/json"}
            x = requests.delete(url, headers=headers)

            return {
                "success": True,
                "message": "your post deleted"
            }, 200
        except Exception as ZZ:
            return {
                "success": False,
                "message": "{0}".format(ZZ)
            }, 400

    # edit post
    def put(self, typo, postID):

        print(typo)

        # if(typo == "like"):
        return self.likeClicked(postID)

        # else:
        #     return self.editPost(postID)

    # 1 to be fixed
    def editPost(self, postID):
        try:
            print("edit post")

            uid = request.json.get('uid')
            text = request.json.get('text')
            images = request.json.get('images')

            if((uid == None) | (text == None)):
                print("in if err")
                return {
                    "success": False,
                    "message": "Missing data"
                }
            else:
                # user= db.reference(path='users/{0}'.format(uid)).get()
                # print(user)
                db.reference(path='community/{0}/postID'.format(postID)).update({
                    "text": text,
                    "images": images
                })

            return {
                "success": True,
                "message": "edited post"
            }

        except Exception as f:
            return {
                "success": False,
                "message": "{0}".format(f)
            }, 400

    # like the post
    def likeClicked(self, postID):
        try:
            uid = request.json.get('uid')

            if((uid == None)):
                return {
                    "success": False,
                    "message": "Missing data"
                }

            post = db.reference(
                path='community/{0}'.format(postID)).get()

            likes = None
            if "likes" in post.keys():
                likes = post["likes"]
            print(post)

            newLikes = []
            if(likes is None):
                newLikes = [uid]
                db.reference(path='community/{0}'.format(postID)).update({
                    "likes": newLikes
                })

            else:
                isFound = False

                for i in likes:
                    if(i != uid):
                        newLikes.append(i)

                    else:
                        isFound = True

                if (isFound == False):
                    newLikes.append(uid)

                db.reference(path='community/{0}'.format(postID)).update({
                    "likes": newLikes
                })

            likesCount = len(newLikes)
            imagesDict = {}
            if "images" in post.keys():
                images = post["images"]
                imagesDict = {i: images[i] for i in range(len(images))}

            url = 'http://18.222.72.221:9200/posts/post/{0}'.format(postID)

            post["likes"] = likesCount
            post["images"] = imagesDict

            headers = {"Content-Type": "application/json"}
            x = requests.put(url, data=json.dumps(post), headers=headers)
            print(x.text)

            return {
                "success": True,
                "message": "post"
            }
        except Exception as VV:
            return {
                "success": False,
                "message": "{0}".format(VV)
            }


communityView = Community.as_view('community')
routes.add_url_rule('/community/<comID>',
                    view_func=communityView, methods=['post', 'get'])
routes.add_url_rule('/community/<comID>/<postID>',
                    view_func=communityView, methods=['delete', 'get', 'put'])


class comments(MethodView):
    # Make comment
    def post(self, postID):
        try:
            uid = request.json.get('uid')
            text = request.json.get('text')
            timeStamp = request.json.get('timeStamp')
            images = request.json.get('images')

            if((uid == None) | (text == None) | (timeStamp == None)):
                return {
                    "success": False,
                    "message": "Missing data"
                }

            else:
                user = db.reference(path='/users/{0}'.format(uid)).get()

                db.reference(path='community/{0}/comments'.format(postID)).push({
                    "text": text,
                    "images": images,
                    "timeStamp": timeStamp,
                    "name": "{0} {1}".format(user["firstName"], user["lastName"]),
                    "avatar": user["avatar"],
                    "uid": uid
                })

                return {
                    "success": True,
                    "message": "comment added"
                }

        except Exception as f:
            return {
                "success": False,
                "message": "{0}".format(f)
            }, 400

    # delete comment
    def delete(self, postID=None, commentID=None):
        try:
            db.reference(
                path='community/{0}/comments/{1}'.format(postID, commentID)).delete()
            return {
                "success": True,
                "message": "your comment deleted"
            }, 200
        except Exception as ZZ:
            return {
                "success": False,
                "message": "{0}".format(ZZ)
            }, 400

    # edit comment
    def put(self, postID=None, commentID=None):
        try:
            uid = request.json.get('uid')
            voteType = request.json.get('voteType')

            if((uid == None) | (voteType == None)):
                return {
                    "success": False,
                    "message": "Missing data"
                }
            else:
                votes = db.reference(
                    path='community/{0}/comments/{1}/votes'.format(postID, commentID)).get()

                up = None
                down = None
                if "up" in votes.keys():
                    up = vote["up"]

                if "down" in votes.keys():
                    down = vote["down"]


                # if (voteType == "up"):
                    

                # else:
                #     pass
            newLikes = []
            if(likes is None):
                newLikes = [uid]
                db.reference(path='community/{0}'.format(postID)).update({
                    "likes": newLikes
                })

            else:
                isFound = False

                for i in likes:
                    if(i != uid):
                        newLikes.append(i)

                    else:
                        isFound = True

                if (isFound == False):
                    newLikes.append(uid)


                db.reference(path='community/{0}/comments/{1}'.format(postID, commentID)).update({
                    "text": text,
                    "images": images
                })

            return {
                "success": True,
                "message": "edited comment"
            }

        except Exception as f:
            return {
                "success": False,
                "message": "{0}".format(f)
            }, 400


commentsView = comments.as_view('comments')
routes.add_url_rule('/comments/<postID>',
                    view_func=commentsView, methods=['post'])
routes.add_url_rule('/comments/<postID>/<commentID>',
                    view_func=commentsView, methods=['delete', 'put'])
