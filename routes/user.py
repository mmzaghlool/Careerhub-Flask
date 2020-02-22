from flask import Flask, request, jsonify
from firebase_admin import auth, db
import requests
from . import routes 
# import re


#add prexperience
@routes.route('/users/addPreExperience', methods=['POST'])
def addPreExperience():
    try:
        uid=request.json.get('uid')
        description = request.json.get('description')
        title = request.json.get('title')
        link = request.json.get('link')
    
        if((uid == None) | (description== None) | (link == None) | (title== None)):
            return {
                "success": False,
                "message": "Missing data"
            }
        else: 
            db.reference(path='users/{0}/preExperience'.format(uid)).push({
                "link": link,
                "title": title,
                "description": description
            })
            return {
                "success": True,
                "message": "your prexperience added perfectly"
            }, 200
    except Exception as MNM:
        return {
            "success": False,
            "message": "{0}".format(MNM)
        }, 400  


#DELETE prexperience
@routes.route('/users/deletePreExperience/<uid>/<key>', methods=['DELETE'])
def deletePreExperience(uid = None, key = None):
    try:
        db.reference(path='users/{0}/preExperience/{1}'.format(uid,key)).delete()
        return {
            "success": True,
            "message": "your experience deleted"
        }, 200
    except Exception as XX:
        return {
            "success": False,
            "message": "{0}".format(XX)
        }, 400  

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
            reportfromuser = db.reference(path='reports/{0}'.format(timestamp)).set({
                "text": text,
                "uid": uid
            })
            return {
                "success": True,
                "message": "your report sent ! thanks for your feedback"
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
                "message": "your link added perfectly"
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
            "message": "your link deleted"
        }, 200
    except Exception as ND:
        return {
            "success": False,
            "message": "{0}".format(ND)
        }, 400  

# Add Project 
@routes.route('/users/addProject', methods=['POST'])
def addProject():
    try:
        uid = request.json.get('uid')
        title=request.json.get('title')
        description = request.json.get('description')
        link=request.json.get('link')
    
        if((uid == None) | (title== None) | (description == None)):
            return {
                "success": False,
                "message": "Missing data"
            }
        else: 
            db.reference(path='users/{0}/projects'.format(uid)).push({
                "title": title,
                "link": link,
                "description": description
            })
            return {
                "success": True,
                "message": "your project added perfectly"
            }, 200
    except Exception as VV:
        return {
            "success": False,
            "message": "{0}".format(VV)
        }, 400   

#DELETE project
@routes.route('/users/deleteProject/<uid>/<key>', methods=['DELETE'])
def deleteProject(uid = None, key=None):
    try:
        db.reference(path='users/{0}/projects/{1}'.format(uid,key)).delete()
        return {
            "success": True,
            "message": "your project deleted"
        }, 200
    except Exception as DD:
        return {
            "success": False,
            "message": "{0}".format(DD)
        }, 400  

#add work
@routes.route('/users/addWork', methods=['POST'])
def addWork():
    try:
        uid=request.json.get('uid')
        description = request.json.get('description')
        title = request.json.get('title')
        startTimestamp = request.json.get('startTimestamp')
        endTimestamp = request.json.get('endTimestamp')
        
        if((uid == None) | (description== None) | (title== None) | (startTimestamp== None) | (endTimestamp== None)):
            return {
                "success": False,
                "message": "Missing data"
            }
        else: 
            db.reference(path='users/{0}/works'.format(uid)).push({
                "startTimestamp": startTimestamp,
                "endTimestamp": endTimestamp,
                "title": title,
                "description": description
            })
            return {
                "success": True,
                "message": "your work added perfectly"
            }, 200
    except Exception as UX:
        return {
            "success": False,
            "message": "{0}".format(UX)
        }, 400  

#delete work
@routes.route('/users/deleteWork/<uid>/<key>', methods=['DELETE'])
def deletework(uid = None, key=None):
    try:
        db.reference(path='users/{0}/works/{1}'.format(uid,key)).delete()
        return {
            "success": True,
            "message": "your work deleted"
        }, 200
    except Exception as ZZ:
        return {
            "success": False,
            "message": "{0}".format(ZZ)
        }, 400

#add skill
@routes.route('/users/addSkill', methods=['POST'])
def addSkill():
    try:
        uid=request.json.get('uid')
        skill=request.json.get('skill')
       
        if((uid == None) | (skill== None)):
            return {
                "success": False,
                "message": "Missing data"
            }
        else: 
            key = db.reference(path='users/{0}/skills'.format(uid)).push().key
            db.reference(path='users/{0}/skills'.format(uid)).update({
                key: skill
            })
            return {
                "success": True,
                "message": "your skill added perfectly"
            }, 200
    except Exception as OO:
        return {
            "success": False,
            "message": "{0}".format(OO)
        }, 400  

#delete Skill
@routes.route('/users/deleteSkills/<uid>/<key>', methods=['DELETE'])
def deleteskills(uid = None, key=None):
    try:
        db.reference(path='users/{0}/skills/{1}'.format(uid,key)).delete()
        return {
            "success": True,
            "message": "your skill deleted"
        }, 200
    except Exception as TT:
        return {
            "success": False,
            "message": "{0}".format(TT)
        }, 400 

#update the date 
@routes.route('/users/updateUser/<uid>', methods=['PUT'])
def updateUser(uid = None):
    try:
        firstName = request.json.get('firstName')
        lastName = request.json.get('lastName')
        phoneNumber = request.json.get('phoneNumber')
        email = request.json.get('email')
        
        if ((firstName == None) | (lastName == None) | (phoneNumber == None) | (uid == None) | (email == None)):
            return {
                "success": False,
                "message": "wrong or missing data"
            }, 400
        else:
            # Update user in auth
            auth.update_user(
                uid,
                email= email,
                phone_number= phoneNumber,
                # password='newPassword',
                display_name=firstName + ' ' + lastName)

            # update user in database
            userData = db.reference(path='users/{0}'.format(uid)).update({
                "firstName": firstName,
                "lastName": lastName,
                "phoneNumber": phoneNumber,
                "email": email,
            }) 
            return {
                "success": True,
                "message": "updateuser completed"
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

#get user
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

@routes.route('/users/answersOfQuestions/<uid>', methods=['POST'])
def answersOfQuestions(uid = None):
    answers = request.json.get('answers')
    maxima=-1     #highest value in answers
    
    for key in answers:
        value=answers["{0}".format(key)]
        
        if (maxima<value):
            maxima=value
    
    x = maxima  # highest percentage skill according to test  
   
    Naturalist = answers["Naturalist"] 
    Musical = answers["Musical"]
    Logical = answers["Logical"]
    Interpersonal = answers["Interpersonal"] 
    Kinesthetic = answers["Kinesthetic"]
    Verbal = answers["Verbal"]
    visual = answers["Visual"]

    print("{0}-{1}-{2}-{3}-{4}-{5}-{6}- {7}".format(Naturalist, Musical, Logical, Interpersonal, Kinesthetic, Verbal, visual, x))
    
    farwlaya = ""
    if(x == Naturalist):
        if(Musical >0.5 and Logical > 0.5 and Kinesthetic > 0.5):
            farwlaya = "Data Administration"
        elif(Interpersonal > 0.5 and Verbal > 0.5 and Interpersonal > 0.5):
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
        if(Naturalist > 0.5 and Verbal > 0.5 and Interpersonal > 0.5):
            farwlaya ="Information Technology"
        elif(Interpersonal > 0.5 and Kinesthetic >0.5 and Visual > 0.5):
            farwlaya ="Ui Developer"
        else: 
            farwlaya ="Web Developer"
    elif (x == Kinesthetic):
        if(Interpersonal > 0.5 and Interpersonal > 0.5 and Visual > 0.5):
            farwlaya ="Ui Developer"
        else:
            farwlaya ="Data Administration"
    elif (x == Verbal):
        if(Naturalist > 0.5 and Interpersonal > 0.5 and Interpersonal > 0.5):
            farwlaya ="Information Technology"
        elif(Interpersonal > 0.5 and Visual > 0.5):
            farwlaya ="Web Developer"
        else: 
            farwlaya ="Mobile Development"
    elif (x == Interpersonal):
        if(Naturalist > 0.5 and Interpersonal > 0.5 and Verbal > 0.5):
            farwlaya ="Information Technology"
        else: 
            farwlaya ="Ui Developer"
    elif (x == Visual):
        if(Verbal > 0.5 and Musical >0.5 ):
            farwlaya ="Mobile Development"
        elif(Interpersonal > 0.5 and Interpersonal > 0.5 and Kinesthetic > 0.5):
            farwlaya ="Ui Developer"
        else: 
            farwlaya ="Web Developer"
    else: 
        farwlaya ="Take Quiz Again"

    return {
        "success": True,
        "response": farwlaya
    }, 200

# upload photo
@routes.route('/users/uploadAvatar/<uid>', methods=['PUT'])
def uploadphoto(uid):
    try:
        link = request.json.get('avatar')

        if((link == None)):
            return {
                "success": False,
                "message": "undefined link"
            }

        ref = db.reference(path='users/{0}'.format(uid))
        ref.update({
            'avatar': link
        })

        return {
            "success": True,
            "message": "photo uploaded"
        }
    except Exception as TY:
        return {
            "success": False,
            "message": "{0}".format(TY)
        }

   

