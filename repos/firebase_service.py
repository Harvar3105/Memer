import firebase_admin
from firebase_admin import credentials, firestore_async
from domain.Metadata import Metadata
import traceback

cred = credentials.Certificate("./firebaseKey.json")
firebase_admin.initialize_app(cred)

db_client = firestore_async.client()
collection_name = "video_memes"

async def test_connection():
  try:
    # Attempt to fetch a document to test the connection
    await db_client.collection(collection_name).limit(1).get()
    return True
  except Exception as e:
    print("Error in test_connection:", e)
    import traceback
    traceback.print_exc()
    return False

async def exists(key:str):
  try:
    snapshot = await db_client.collection(collection_name).document(key).get()
    return snapshot.exists
  except Exception as e:
    print("Error in list_files:", e)
    traceback.print_exc()
    return False

async def save_video_metadata(video: Metadata):
  try:
    return await db_client.collection(collection_name).document(video.key).set(video.to_dict())
  except Exception as e:
    print("Error in list_files:", e)
    traceback.print_exc()
    return None

async def get_video_metadata(key: str) -> Metadata:
  try:
    doc = await db_client.collection(collection_name).document(key).get()

    if doc.exists :
      return Metadata.from_dict(doc.to_dict())
    else:
      return None
  except Exception as e:
    print("Error in list_files:", e)
    traceback.print_exc()
    return None
