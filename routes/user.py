from flask import Flask, request, jsonify
from firebase_admin import auth, db
import requests
from . import routes 
import re


# (2) upload image >>> 7ta5dy mn el user el link bta3 download el image w t7oteh gwa el profile bta3 el user esmo "avatar"


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
  
  


#   //////////////
@routes.route('/users/getQuestions', methods=['GET'])
def getQuestions():
    try:      
        # get questions
        questions = db.reference(path='questions').get()

        return {
            "success": True,
            "questions": questions
        }, 200
    except Exception as e:
        return {
            "success": False,
            "message": "{0}".format(e)
        }, 400



#**************
@routes.route('/users/answersOfQuestions/<uid>', methods=['POST'])
def answersOfQuestions(uid = None):
    answers = request.json.get('answers')
    maxima=-1     #highest value in answers
    
    for key in answers:
        value = answers[key]
        if (maxima<value):
            maxima=value
    
    x = maxima  # highest percentage skill according to test  
   
    Naturalist = answers["Naturalist"]
    Musical = answers["Musical"]
    Logical = answers["Logical"]
    Interpersonal = answers["Interpersonal"] 
    Kinesthetic = answers["Kinesthetic"]
    Verbal = answers["Verbal"]
    Visual = answers["Visual"]
    
   
    farwlaya = ""
    if(x == Naturalist):
        if(Musical >0.5 and Logical > 0.5 and Kinesthetic > 0.5):
            farwlaya = "Data Administration"
        elif(Interpersonal > 0.5 and Verbal > 0.5 and Intrapersonal > 0.5):
            farwlaya="Information Technology"
        else: 
            farwlaya ="Network Engineer"
    elif (x == Musical):
        if(Naturalist > 0.5 and Logical > 0.5 and Kinesthetic > 0.5 ):
            farwlaya ="Data Administration"
        elif(Naturalist > 0.5 and Logical > 0.5):
            farwlaya ="Network Engineer"
        else: 
            farwlaya ="Mobile Development"
    elif (x == Logical):
        if(Naturalist > 0.5 and Musical > 0.5 and Kinesthetic > 0.5):
            farwlaya ="Data Administration"
        else:
            farwlaya ="Network Engineer"
    elif (x == Interpersonal):
        if(Naturalist > 0.5 and Verbal > 0.5 and Intrapersonal > 0.5):
            farwlaya ="Information Technology"
        elif(Intrapersonal > 0.5 and Kinesthetic >0.5 and Visual > 0.5):
            farwlaya ="Ui Developer"
        else: 
            farwlaya ="Web Developer"
    elif (x == Kinesthetic):
        if(Intrapersonal > 0.5 and Interpersonal > 0.5 and Visual > 0.5):
            farwlaya ="Ui Developer"
        else:
            farwlaya ="Data Administration"
    elif (x == Verbal):
        if(Naturalist > 0.5 and Interpersonal > 0.5 and Intrapersonal > 0.5):
            farwlaya ="Information Technology"
        elif(Interpersonal > 0.5 and Visual > 0.5):
            farwlaya ="Web Developer"
        else: 
            farwlaya ="Mobile Development"
    elif (x == Intrapersonal):
        if(Naturalist > 0.5 and Interpersonal > 0.5 and Verbal > 0.5):
            farwlaya ="Information Technology"
        else: 
            farwlaya ="Ui Developer"
    elif (x == Visual):
        if(Verbal > 0.5 and Musical >0.5 ):
            farwlaya ="Mobile Development"
        elif(Intrapersonal > 0.5 and Interpersonal > 0.5 and Kinesthetic > 0.5):
            farwlaya ="Ui Developer"
        else: 
            farwlaya ="Web Developer"
    else: 
        farwlaya ="Take Quiz Again"

    return {
        "success": True,
        "response": farwlaya
    }, 200
