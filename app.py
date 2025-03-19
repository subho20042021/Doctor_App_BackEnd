from flask import Flask, jsonify
import firebase_admin
from firebase_admin import firestore, credentials


cred = credentials.Certificate('admin.json')
firebase_admin.initialize_app(cred)

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/data', methods = ['POST'])
def getDepartmentData():


    db = firestore.client()

    db_ref = db.collection('Department').stream()
    return jsonify(list(map(lambda doc: doc.to_dict(), db_ref)))





if __name__ == '__main__':
    app.run()
