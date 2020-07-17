from flask import Flask, request, jsonify
from firebase_admin import auth, db
import requests
from . import routes


@routes.route('/chat/sendMessage', methods=['POST'])
def createMsg():

    senderUid = request.json.get('senderUid')
    receiverUid = request.json.get('receiverUid')
    message = request.json.get('message') 
    timestamp = request.json.get('timestamp')
    image = request.json.get('image')

    if((senderUid==None) | (receiverUid==None) | (message==None) | (timestamp==None)):
        return {
            "success":False,
            "message":"Missing data"
        }
            
    roomKey = db.reference('messagesHeads/{0}/{1}/roomKey'.format(senderUid, receiverUid)).get()

    if (roomKey == None):
        roomKey = db.reference('messages').push("new Message").key
        
        senderUser = db.reference('users/{0}'.format(senderUid)).get()
        receiverUser = db.reference('users/{0}'.format(receiverUid)).get()

        db.reference('messagesHeads/{0}/{1}'.format(senderUid, receiverUid)).update({
            "avatar": receiverUser["avatar"],
            "roomKey": roomKey,
            "name": "{0} {1}".format(receiverUser["firstName"], receiverUser["lastName"])
        })

        db.reference('messagesHeads/{0}/{1}'.format(receiverUid, senderUid)).update({
            "avatar": senderUser["avatar"],
            "roomKey": roomKey,
            "name": "{0} {1}".format(senderUser["firstName"], senderUser["lastName"])
        })

    messageObj = {
        "message": message,
        "senderUid": senderUid
    }
    if (image != None):
        messageObj["image"] = image

    db.reference('messages/{0}/{1}'.format(roomKey, timestamp)).update(messageObj)

    return {
        "success": True,
        "message": "Message created {0}".format(roomKey),
        "roomKey": roomKey
    }

#chat list
@routes.route('/chat/list/<uid>', methods=['GET'])
def chatlist(uid):
    try:
        userMessages = db.reference(path='messagesHeads/{0}'.format(uid)).get()

        return {
            "success": True,
            "message": "Messanger list sent",
            "data": userMessages,
        }, 200
    except Exception as NMN:
        return {
            "success": False,
            "message": "{0}".format(NMN)
        }, 400  

#chat roomId
@routes.route('/chat/roomID/<senderUid>/<receiverUid>', methods=['GET'])
def roomID(senderUid, receiverUid):
    try:
        chatHead = db.reference(path='messagesHeads/{0}/{1}'.format(senderUid, receiverUid)).get()

        return {
            "success": True,
            "message": "Chathead sent",
            "data": chatHead,
        }, 200

    except Exception as NMN:
        return {
            "success": False,
            "message": "{0}".format(NMN)
        }, 400  