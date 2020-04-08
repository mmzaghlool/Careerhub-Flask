from flask import Flask, request, jsonify
from flask.views import MethodView
from firebase_admin import auth, db
import requests
from . import routes
import moment
from datetime import datetime
import time
import math

'''
4. search in courses and profiles GET
5. Leave group DELETE
6. send message to the group
7. modify the progress
8. add community id
'''


class Groups(MethodView):
    def get(self, uid, groupID):
        try:
            print('get', groupID)

            if uid is not None:
                result = {}
                userGroups = db.reference(path='users/{0}/groups'.format(uid)).get()

                for groupID in userGroups:
                    group = db.reference(path='groups/{0}'.format(groupID)).get()
                    result[groupID] = group

                return {
                           "success": True,
                           "message": "Data sent",
                           "data": result
                       }, 200


            # return a list of groups for specific user
            if groupID is None:
                groups = db.reference(path='groups').get()

                return {
                           "success": True,
                           "message": "Data sent",
                           "data": groups
                       }, 200

            # return specific group
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

    # enroll in course
    def post(self):
        uid = request.json.get('uid')
        courseID = request.json.get('courseID')
        print("uid, courseID", uid, courseID)

        try:
            # Get course data
            courseData = db.reference(
                path='courses/{0}'.format(courseID)).get()

            # Get last group assigned to that course
            lastCourse = db.reference(path='groups').order_by_child(
                'courseID').equal_to(courseID).limit_to_last(1).get()

            key = None
            if (lastCourse != None):
                for key in lastCourse:
                    print(key)

            # get last group opened in this course
            lastTimestamp = None
            lastMembers = None
            currentTimestamp = math.floor(time.time())

            if (key != None):
                lastCourse = lastCourse[key]
                # lastCourse = dict(lastCourse)
                lastMembers = len(lastCourse["members"])
                lastTimestamp = lastCourse["startTimestamp"]

            print("-----------------------------")
            print(lastTimestamp, lastMembers)

            user = db.reference('users/{0}'.format(uid)).get()

            if ((lastMembers != None) & (lastMembers != None)):
                if ((lastMembers < 5) & (lastTimestamp < (currentTimestamp + 7 * 24 * 60 * 60))):
                    return joinCurrentGroup(uid, key, courseData, lastCourse, lastMembers, currentTimestamp, user)
                else:
                    return startNewGroup(uid, courseID, courseData, currentTimestamp, user)

            else:
                return startNewGroup(uid, courseID, courseData, user)

        except Exception as NMN:
            print("{0}".format(NMN))
            # startNewGroup(uid    , courseID)
            return {
                       "success": False,
                       "message": "{0}".format(NMN)
                   }, 400

    # TODO
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

    # TODO
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


def startNewGroup(uid=None, courseID=None, courseData=None, currentTimestamp=None, user=None):
    print("startNEwGroup")

    # get new chat key
    chatKey = db.reference('messages').push({
        "message": "Chat started",
        "senderUid": uid
    }).key

    # Update group data
    group = {
        "members": {uid: {
            "name": "{0} {1}".format(user.firstName, user.lastName),
            "avatar": user.avatar,
        }},
        "startTimestamp": currentTimestamp,
        "chat": chatKey,
        "Community": 'id',
        "progress": {uid: {"x": True}},
        "courseID": courseID
    }
    groupKey = db.reference(path='groups').push(group).key

    print(chatKey)

    # update user data
    addDataToDB(uid, group, courseData, groupKey)

    return {
               "success": True,
               "message": "Data uploaded",
           }, 200


def joinCurrentGroup(uid, key, courseData, lastCourse, lastMembers, currentTimestamp, user):
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

    addDataToDB(uid, lastCourse, courseData, key)

    return {
               "success": True,
               "message": "Data uploaded",
           }, 200


def addDataToDB(uid, lastCourse, courseData, groupID):
    # update user chat
    db.reference('users/{0}/messages/{1}'.format(uid, groupID)).update({
        # "avatar": receiverUser["avatar"],
        "roomKey": lastCourse["chat"],
        "name": "{0}".format(courseData["title"])
    })

    # update user groups
    db.reference('users/{0}/groups/{1}'.format(uid, groupID)).update({
        # "pic": avatar, 
        "title": courseData["title"],
        "courseID": courseData["courseID"],
        "groupID": groupID
    })


# routes.add_url_rule('/courses/', view_func=Courses.as_view('courses'))

user_view = Groups.as_view('groups')
routes.add_url_rule('/groups/<string:uid>', defaults={'groupID': None},
                    view_func=user_view, methods=['GET', ])
routes.add_url_rule('/groups/', view_func=user_view, methods=['POST', ])
routes.add_url_rule('/groups/<string:groupID>', view_func=user_view,
                    methods=['GET', 'PUT', 'DELETE'])
