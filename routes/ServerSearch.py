from flask import Flask, request, jsonify
import requests
import json
from . import routes


@routes.route('/search/<query>', methods=['GET'])
def search(query):
    try:
        url = 'http://18.222.72.221:9200/_search?q={0}'.format(query)
        headers = {"Content-Type": "application/json"}
        x = requests.get(url, headers=headers)

        return {
            "success": True,
            "message": "Data sent",
            "data": x.text
        }, 200

    except Exception as NMN:
        return {
            "success": False,
            "message": "{0}".format(NMN)
        }, 400


@routes.route('/searchCourses/<query>', methods=['GET'])
def searchCourses(query=None):
    print(query)
    try:
        url = 'http://18.222.72.221:9200/courses/course/_search?q={0}'.format(query)
        headers = {"Content-Type": "application/json"}
        x = requests.get(url, headers=headers)

        return {
            "success": True,
            "message": "Data sent",
            "data": x.text
        }, 200

    except Exception as NMN:
        return {
            "success": False,
            "message": "{0}".format(NMN)
        }, 400

@routes.route('/searchUsers/<query>', methods=['GET'])
def searchUsers(query=None):
    print(query)
    try:
        url = 'http://18.222.72.221:9200/users/user/_search?q={0}'.format(query)
        headers = {"Content-Type": "application/json"}
        x = requests.get(url, headers=headers)

        return {
            "success": True,
            "message": "Data sent",
            "data": x.text
        }, 200

    except Exception as NMN:
        return {
            "success": False,
            "message": "{0}".format(NMN)
        }, 400

@routes.route('/coursesInExactTrack/<track>', methods=['GET'])
def coursesInExactTrack(track=None):
    print(track)
    try:
        url = 'http://18.222.72.221:9200/courses/course/_search'
        obj = {
            "query": {
                "match_phrase": {
                    "genres":  track
                }
            }
        }

        headers = {"Content-Type": "application/json"}
        x = requests.get(url, data=json.dumps(obj), headers=headers)

        return {
            "success": True,
            "message": "Data sent",
            "data": x.text
        }, 200

    except Exception as NMN:
        return {
            "success": False,
            "message": "{0}".format(NMN)
        }, 400
