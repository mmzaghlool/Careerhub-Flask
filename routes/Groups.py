from flask import Flask, request, jsonify
from flask.views import MethodView
from firebase_admin import auth, db
import requests
from . import routes
import moment
from datetime import datetime
import time
import math


# '''
# 1. enroll in course POST
# 2. get all courses GET
# 3. get specific group GET
# 4. search in courses and profiles GET
# '''

class Groups(MethodView):
    def get(self, groupID):
        try:
            print('get', groupID)
            if groupID is None:
                # return a list of users
                groups = db.reference(path='groups').get()

                return {
                    "success": True,
                    "message": "Data sent",
                    "data": groups
                }, 200

            else:
                group = db.reference(path='groups/{0}'.format(groupID)).get()

                return {
                    "success": True,
                    "message": "Data sent",
                    "data": group
                }, 200

        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400

    def startNewGroup(self, uid=None, courseID=None, courseData=None, currentTimestamp=None, user=None):
        print("startNEwGroup")
        print(courseData)
        print(currentTimestamp)

        # get new chat key
        chatKey = db.reference('messages').push({
            "message": "Chat started",
            "senderUid": uid
        }).key

        print("'''''''''chatKey'''''''''")
        groupKey = db.reference(path='groups').push({
            "members": {uid: {
                "name": "{0} {1}".format(user.firstName, user.lastName),
                "avatar": user.avatar,
            }},
            "startTimestamp": currentTimestamp,
            "chat": chatKey,
            "Community": 'id',
            "progress": {uid: {"x": True}},
            "courseID": courseID
        }).key

        print(chatKey)

        db.reference('users/{0}/messages/{1}'.format(uid, groupKey)).update({
            # "avatar": receiverUser["avatar"],
            "roomKey": chatKey,
            "name": "{0}".format(courseData["title"])
        })

        return {
            "success": True,
            "message": "Data uploaded",
        }, 200



    def joinCurrentGroup(self, uid=None, key=None, courseData=None, lastCourse=None, lastMembers=None, currentTimestamp=None, user=None):

        members = lastCourse["members"]
        members[uid] = {
            "name": "{0} {1}".format(user.firstName, user.lastName),
            "avatar": user.avatar,
        }
        lastCourse["members"] = members

        # add user to progress list
        progress = lastCourse["progress"]
        progress[uid] = {"x": True}
        lastCourse["progress"] = progress

        # update data in db
        db.reference(path='groups/{0}'.format(key)).update(lastCourse)

        # update user chat
        db.reference('users/{0}/messages/{1}'.format(uid, key)).update({
            # "avatar": receiverUser["avatar"],
            "roomKey": lastCourse["chat"],
            "name": "{0}".format(courseData["title"])
        })

        db.reference('users/{0}/groups/{1}'.format(uid, key)).update({
            # TODO make it real
        })
        return {
            "success": True,
            "message": "Data uploaded",
        }, 200

    # enroll in course
    def post(self):

        uid=request.json.get('uid')
        courseID=request.json.get('courseID')
        print(uid, courseID)
        try:
            # Get course data
            courseData=db.reference(
                path='courses/{0}'.format(courseID)).get()

            # Get last group assigned to that course
            lastCourse=db.reference(path='groups').order_by_child(
                'courseID').equal_to(courseID).limit_to_last(1).get()

            key=None
            if (lastCourse != None):
                for key in lastCourse:
                    print(key)

            # get last group opened in this course
            lastTimestamp=None
            lastMembers=None
            currentTimestamp=math.floor(time.time())

            if (key != None):
                lastCourse=lastCourse[key]
                # lastCourse = dict(lastCourse)
                lastMembers=len(lastCourse["members"])
                lastTimestamp=lastCourse["startTimestamp"]

            print("-----------------------------")
            print(lastTimestamp, lastMembers)

            user = db.reference('users/{0}'.format(uid)).get()


            if ((lastMembers != None) & (lastMembers != None)):
                if ((lastMembers < 5) & (lastTimestamp < (currentTimestamp + 7*24*60*60))):
                    return self.joinCurrentGroup(uid, key, courseData, lastCourse, lastMembers, currentTimestamp, user)
                else:
                    return self.startNewGroup(uid, courseID, courseData, currentTimestamp, user)

            else:
                return self.startNewGroup(uid, courseID, courseData, user)

        except Exception as NMN:
            print("{0}".format(NMN))
            # self.startNewGroup(uid    , courseID)
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400

    def delete(self, groupID):
        try:
            # delete a single user
            db.reference(path='groups/{0}'.format(groupID)).delete()
            return {
                "success": True,
                "message": "course deleted",
            }, 200
        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400

    def put(self, groupID):
        try:
            # update a single user
            db.reference(path='groups/{0}'.format(groupID)).update({
                "director": request.json.get('director'),
                "genres": request.json.get('genres'),
                "instructor": request.json.get('instructor'),
                "keywords": request.json.get('keywords'),
                "lastUpdated": request.json.get('lastUpdated'),
                "overview": request.json.get('overview'),
                "popularity": request.json.get('popularity'),
                "language": request.json.get('language'),
                "runtime": request.json.get('runtime'),
                "title": request.json.get('title'),
                "url": request.json.get('url'),
                "vote_average": request.json.get('vote_average'),
            })
            return {
                "success": True,
                "message": "Data uploaded",
            }, 200
        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400


# routes.add_url_rule('/courses/', view_func=Courses.as_view('courses'))

user_view=Groups.as_view('groups')
routes.add_url_rule('/groups/', defaults={'groupID': None},
                    view_func=user_view, methods=['GET', ])
routes.add_url_rule('/groups/', view_func=user_view, methods=['POST', ])
routes.add_url_rule('/groups/<string:groupID>', view_func=user_view,
                    methods=['GET', 'PUT', 'DELETE'])
