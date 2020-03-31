from flask import Flask, request, jsonify
from flask.views import MethodView
from firebase_admin import auth, db
import requests
from . import routes

import time
import math

class Notifications(MethodView):
    def get(self, uid):
        try:
            print('get', uid)

            notifications = db.reference(path='notifications').order_by_child("receiverUID").equal_to(uid).get()

            return {
                "success": True,
                "message": "Data sent",
                "data": notifications
            }, 200
           
        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400


    def post(self):
        try:
            currentTimestamp=math.floor(time.time())

            # create a new Course 
            db.reference(path='notifications').push({
                "receiverUID":request.json.get('receiverUID'),
                "senderUID": request.json.get('senderUID'),
                "title": request.json.get('title'), 
                "body": request.json.get('body'),
                "image": request.json.get('image'),
                "sendTime": currentTimestamp,
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

    def delete(self, uid):
        try:
            # delete token
            deviceID = request.json.get('deviceID')
            db.reference(path='tokens/{0}/{1}'.format(uid, deviceID)).delete()
            return {
                "success": True,
                "message": "Token deleted",
            }, 200           
        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400  

    def put(self, uid):
        try:
            deviceID = request.json.get('deviceID')
            playerID = request.json.get('playerID')

            # add token to database
            db.reference(path='tokens/{0}'.format(uid)).update({
                deviceID: playerID
            })

            return {
                "success": True,
                "message": "Token uploaded",
            }, 200           
        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }, 400  


# routes.add_url_rule('/notifications/', view_func=Notifications.as_view('notifications'))

user_view = Notifications.as_view('notifications')
routes.add_url_rule('/notifications/', view_func=user_view, methods=['POST',])
routes.add_url_rule('/notifications/<string:uid>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])
