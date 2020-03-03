from flask import Flask, request, jsonify
from flask.views import MethodView
from firebase_admin import auth, db
import requests
from . import routes

class Courses(MethodView):
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

user_view = Courses.as_view('courses')
routes.add_url_rule('/courses/', defaults={'courseID': None},
                 view_func=user_view, methods=['GET',])
routes.add_url_rule('/courses/', view_func=user_view, methods=['POST',])
routes.add_url_rule('/courses/<string:courseID>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])