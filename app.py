from flask import Flask, request
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials, firestore, auth, db
# from "./src/auth" import auth
app = Flask(__name__)
CORS(app)

from routes import *
app.register_blueprint(routes)
# app.register_blueprint(auth)

# Use the application default credentials
cred = credentials.Certificate('./aiet-bae93-13ecac79617e.json')
firebase_admin.initialize_app(cred, {"databaseURL": "https://aiet-bae93.firebaseio.com/"})


@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)