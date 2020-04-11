from flask import request
from flask.views import MethodView
from firebase_admin import db
import re

from . import routes
import time
import math


# TODO: update community id "course enrollment"


class Groups(MethodView):

    def get(self, id):
        try:
            isRoomKey = re.match("-[0-9a-zA-Z]*", id)

            # return a list of groups for specific user
            if not isRoomKey:
                print("get user groups", id)
                result = {}
                userGroups = db.reference(path='users/{0}/groups'.format(id)).get()

                # for groupID in userGroups:
                #     group = db.reference(path='groups/{0}'.format(groupID)).get()
                #     result[groupID] = group

                return {
                           "success": True,
                           "message": "Data sent",
                           "data": userGroups
                       }, 200

            # return specific group
            else:
                print("get group: ", id)
                group = db.reference(path='groups/{0}'.format(id)).get()

                return {
                           "success": True,
                           "message": "Data sent",
                           "data": group
                       }, 200

        except Exception as NMN:
            return {
                "success": False,
                "message": "{0}".format(NMN)
            }

    # enroll in course
    def post(self):
        uid = request.json.get('uid')
        courseID = request.json.get('courseID')
        print('courseID', courseID)
        print('uid', uid)
        try:
            # Check if user already enrolled in this course
            userGroups = db.reference('users/{0}/groups'.format(uid)).get()

            if userGroups is not None:
                for key in userGroups:
                    group = userGroups[key]
                    print("group", group)
                    if group["courseID"] == courseID:
                        return {
                            "success": False,
                            "message": "User already enrolled in this course"
                        }

            # Get course data
            courseData = db.reference(path='courses/{0}'.format(courseID)).get()

            # Get last group assigned to that course
            lastCourse = db.reference(path='groups').order_by_child('courseID') \
                .equal_to(courseID).limit_to_last(1).get()

            key = None
            if lastCourse is not None:
                for key in lastCourse:
                    print(key)

            # get last group opened in this course
            lastTimestamp = None
            lastMembers = None
            currentTimestamp = math.floor(time.time())

            if key is not None:
                lastCourse = lastCourse[key]
                # lastCourse = dict(lastCourse)
                lastMembers = len(lastCourse["members"])
                lastTimestamp = lastCourse["startTimestamp"]

            print("-----------------------------")
            print(lastTimestamp, lastMembers)

            user = db.reference('users/{0}'.format(uid)).get()

            # if there is group available to enroll
            if (lastMembers is not None) & (lastMembers is not None):

                # if course members < 5 and its started < week ago
                if (lastMembers < 5) & (lastTimestamp < (currentTimestamp + 7 * 24 * 60 * 60)):
                    # add this user to the current group
                    return joinCurrentGroup(uid, key, courseData, lastCourse, user, courseID)
                else:
                    # if not .... start new group
                    return startNewGroup(uid, courseID, courseData, currentTimestamp, user)

            # there is no working group
            else:
                return startNewGroup(uid, courseID, courseData, currentTimestamp, user)

        except Exception as NMN:
            print("{0}".format(NMN))
            # startNewGroup(uid    , courseID)
            return {
                       "success": False,
                       "message": "{0}".format(NMN)
                   }

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
    chatKey = db.reference('messages').push().key
    db.reference('messages/{0}'.format(currentTimestamp)).push({
        "message": "Chat started",
        "senderUid": uid
    })

    # Update group data
    group = {
        "members": {uid: {
            "name": "{0} {1}".format(user["firstName"], user["lastName"]),
            "avatar": user["avatar"],
        }},
        "startTimestamp": currentTimestamp,
        "chat": chatKey,
        "Community": 'id',
        "progress": {uid: {"x": False}},
        "courseID": courseID,
        "instructor": courseData["instructor"],
        "director": courseData["director"],
        "genres": courseData["genres"],
        "language": courseData["language"],
        "title": courseData["title"]
    }
    groupKey = db.reference(path='groups').push(group).key

    print(chatKey)

    # update user data
    addDataToDB(uid, group, courseData, groupKey, user, courseID)

    return {
               "success": True,
               "message": "Data uploaded",
           }, 200


def joinCurrentGroup(uid, key, courseData, lastCourse, user, courseID):
    # add this user to the group members
    db.reference(path='groups/{0}/members/{1}'.format(key, uid)).update({
        "name": "{0} {1}".format(user["firstName"], user["lastName"]),
        "avatar": user["avatar"],
    })

    # add this user to the progress
    db.reference(path='groups/{0}/progress/{1}'.format(key, uid)).update({"x": False})

    # update user group data
    addDataToDB(uid, lastCourse, courseData, key, user, courseID)

    return {
               "success": True,
               "message": "Data uploaded",
           }, 200


def addDataToDB(uid, lastCourse, courseData, groupID, user, courseID):
    # update user chat
    db.reference('users/{0}/messages/{1}'.format(uid, groupID)).update({
        "avatar": user["avatar"],
        "roomKey": lastCourse["chat"],
        "name": "{0}".format(courseData["title"])
    })

    # update user groups
    db.reference('users/{0}/groups/{1}'.format(uid, groupID)).update({
        "title": courseData["title"],
        "instructor": courseData["instructor"],
        "director": courseData["director"],
        "genres": courseData["genres"],
        "courseID": courseID
    })


# routes.add_url_rule('/courses/', view_func=Courses.as_view('courses'))

user_view = Groups.as_view('groups')
# routes.add_url_rule('/groups/<string:uid>', defaults={'groupID': None},
#                     view_func=user_view, methods=['GET', ])
routes.add_url_rule('/groups', view_func=user_view, methods=['POST'])
routes.add_url_rule('/groups/<string:id>', view_func=user_view,
                    methods=['GET', 'PUT', 'DELETE'])
