from flask import Flask, request, jsonify
from flask.views import MethodView
from firebase_admin import auth, db
import requests
import json
from . import routes

USERS="users/user"
POSTS="posts/post"
COURSES="courses/courses"

class ElasticSearch(MethodView):
    def get(self, courseID):
        try:
            print('get', courseID)

            if courseID is None:
                # return a list of courses
                courses = db.reference(path='courses').get()

                return {
                    "success": True,
                    "message": "Data sent",
                    "data": courses
                }, 200
                
            else:
                course = db.reference(path='courses/{0}'.format(courseID)).get()

                return {
                    "success": True,
                    "message": "Data sent",
                    "data": course
                }, 200
           
        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400  

    def post(self):
        try:
            # create a new Course 
            db.reference(path='courses').push({
                "director":request.json.get('director'),
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
                "vote_count": request.json.get('vote_count')
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

    def delete(self, courseID):
        try:
            # delete a single user
            db.reference(path='courses/{0}'.format(courseID)).delete()
            return {
                "success": True,
                "message": "course deleted",
            }, 200           
        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400  

    def put(self, courseID):
        try:
            # update a single user
            db.reference(path='courses/{0}'.format(courseID)).update({
                "director":request.json.get('director'),
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

view = ElasticSearch.as_view('elasticSearch')
# routes.add_url_rule('/elasticSearch/', defaults={'courseID': None},
#                  view_func=view, methods=['GET',])
# routes.add_url_rule('/elasticSearch/', view_func=view, methods=['POST',])
routes.add_url_rule('/elasticSearch/index/<string:x>', view_func=view,
                 methods=['GET', 'PUT', 'DELETE', 'POST'])



#index all current courses
@routes.route('/elasticSearch/indexPrev/<index>', methods=['POST'])
def indexPrev(index):
    try:
        data = db.reference(path='{0}'.format(index)).get()

        if index == "users":
            for uid in data:
                user = data[uid]

                url = 'http://18.222.72.221:9200/users/user/{0}'.format(uid)
                obj = {
                    "firstName": "{0}".format(user["firstName"]),
                    "lastName": "{0}".format(user["lastName"]),
                    "email": "{0}".format(user["email"]),
                    "phoneNumber": "{0}".format(user["phoneNumber"]),
                    "uid": "{0}".format(uid),
                }
                print(obj)
                print(url)
                headers = {"Content-Type": "application/json"}
                x = requests.post(url, data=json.dumps(obj), headers=headers)
                print(x.text)

        if index == "courses":
            for key in data:
                course = data[key]
                if course == False:
                    continue

                url = 'http://18.222.72.221:9200/courses/course/{0}'.format(key)
                obj = {
                    "director": course["director"],
                    "genres": course["genres"],
                    "instructor": course["instructor"],
                    "keywords": course["keywords"],
                    "language": course["language"],
                    "overview": course["overview"],
                    "title": course["title"],
                    "url": course["url"],
                    "vote_average": course["vote_average"],
                    "vote_count": int(course["vote_count"].replace(",", "")),
                    "key": key
                }

                print(obj)
                print(url)
                headers = {"Content-Type": "application/json"}
                x = requests.post(url, data=json.dumps(obj), headers=headers)
                print(x.text)

        return {
            "success": True,
            "message": "Messanger list sent",
            "data": data
        }, 200
    except Exception as NMN:
        return {
            "success": False,
            "message": "{0}".format(NMN)
        }, 400  