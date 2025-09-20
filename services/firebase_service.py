import firebase_admin
from firebase_admin import credentials, firestore
from domain.Metadata import Metadata

cred = credentials.Certificate("./firebaseKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db_name = "video_memes"

# def save_user(uid, data):
#     db.collection("users").document(uid).set(data)

# def get_user(uid):
#     doc = db.collection("users").document(uid).get()
#     return doc.to_dict() if doc.exists else None

async def exists(key:str):
  return await db.collection(db_name).document(key).exists()

async def save_video_metadata(video: Metadata):
  success = await db.collection(db_name).document(video.key).set(video)
  return success

async def get_video_metadata(key: str) -> Metadata:
  doc = db.collection(db_name).document(key).get()

  if doc.exists :
    return Metadata.from_dict(doc.to_dict())
  else:
    return None
