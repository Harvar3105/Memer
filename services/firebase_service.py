import firebase_admin
from firebase_admin import credentials, firestore
import os

cred_path = os.getenv("./firebaseKey.json")
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_user(uid, data):
    db.collection("users").document(uid).set(data)

def get_user(uid):
    doc = db.collection("users").document(uid).get()
    return doc.to_dict() if doc.exists else None
