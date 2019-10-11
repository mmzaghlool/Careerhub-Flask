from flask import Flask, request, jsonify
from firebase_admin import auth, db
import requests
from . import routes 
import re

#Serch 
# @routes.route('/searchProfile', methods=['GET'])
# def searchword():
#     try:






#THE REPORT 
@routes.route('/users/reportFromUser', methods=['POST'])
def reportfromuser():
    try:
        uid = request.json.get('uid')
        text = request.json.get('text')
        timestamp = request.json.get('timeStamp')

        if((uid == None) | (text== None) | (timestamp == None) ):
            return {
                "success": False,
                "message": "Missing data"
            }
        else:
            reportfromuser = db.reference(path='Reports/{0}/{1}'.format(uid, timestamp)).set({
                "text": text,
            })
            return {
                "success": True,
                "update": "your report sent ! thanks for your feedback"
            }, 200
    except Exception as NN:
        return {
            "success": False,
            "message": "{0}".format(NN)
        }, 400 


# SOCIAL MEDIA 
@routes.route('/users/addSocialMedia', methods=['POST'])
def addSocialMedia():
    try:
        uid = request.json.get('uid')
        text = request.json.get('text')
        typo = request.json.get('type')
    
        if((uid == None) | (text== None) | (typo == None) ):
            return {
                "success": False,
                "message": "Missing data"
            }
        else: 
            db.reference(path='users/{0}/social'.format(uid)).update({
                typo: text
            })
            return {
                "success": True,
                "update": "your link added perfectly"
            }, 200
    except Exception as DD:
        return {
            "success": False,
            "message": "{0}".format(DD)
        }, 400  



#DELETE SOCIAL MEDIA
@routes.route('/users/deleteSocial/<uid>/<typo>', methods=['DELETE'])
def deletesocial(uid = None, typo=None):
    try:
        db.reference(path='users/{0}/social/{1}'.format(uid,typo)).delete()
        return {
            "success": True,
            "update": "your link deleted"
        }, 200
    except Exception as ND:
        return {
            "success": False,
            "message": "{0}".format(ND)
        }, 400  



#update the date 
@routes.route('/users/updateUser/<uid>', methods=['PUT'])
def updateUser(uid = None):
    try:
        firstName = request.json.get('firstName')
        lastName = request.json.get('lastName')
        phoneNumber = request.json.get('phoneNumber')
        
        # pattern = re.compile("/^[A-Za-z0-9]+$/")
        # isValidUid = re.search("/^[A-Za-z0-9]+$/", uid)
        # print(isValidUid)

        # userData = db.reference(path='users/{0}'.format(uid)).get()
        if ((firstName == None) | (lastName == None) | (phoneNumber == None) | (uid == None)):
            return {
                "success": False,
                "message": "wrong or missing data"
            }, 400
        else:
            userData = db.reference(path='users/{0}'.format(uid)).update({
                "firstName": firstName,
                "lastName": lastName,
                "phoneNumber": phoneNumber
            }) 
            return {
                "success": True,
                "update": "updateuser completed"
            }, 200
    except Exception as DINA:
        return {
            "success": False,
            "message": "{0}".format(DINA)
        }, 400


# POST -- Add data
@routes.route('/users/registerUser', methods=['POST'])
def registerUser():
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    phoneNumber = request.json.get('phoneNumber')

    # check data
    if((firstName == None) | (lastName == None) | (password == None) | (email == None) | (phoneNumber == None)):
        return {
            "success": False,
            "message": "Missing data"
        }
    
    # Create new user
    try:
        user = auth.create_user(
            email=email,
            email_verified=False,
            phone_number=phoneNumber,
            password=password,
            display_name='{0} {1}'.format(firstName, lastName),
            disabled=False
        )

        ref = db.reference(path='users/{0}'.format(user.uid))
        ref.set({
            'email': email,
            'phoneNumber': phoneNumber,
            'firstName': firstName,
            'lastName': lastName,
        })

        return {
            "success": True,
            "message": "User created"
        }
    except Exception as exc:
        return {
            "success": False,
            "message": "{0}".format(exc)
        }


@routes.route('/users/getUser/<uid>', methods=['GET'])
def getUser(uid = None):
    try:      
        # get user data
        userData = db.reference(path='users/{0}'.format(uid)).get()
        print('user',userData)
        if (userData == None):
            return {
                "success": False,
                "message": "wrong uid"
            }, 400
        else:
            return {
                "success": True,
                "user": userData
            }, 200
    except Exception as e:
        return {
            "success": False,
            "message": "{0}".format(e)
        }, 400
  