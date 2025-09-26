from repos.firebase_service import save_video_metadata, exists, test_connection as fb_test
from repos.r2_service import list_files, test_connection as r2_test
from domain.Metadata import Tag

async def test_all_connections():
  r2_connection = await r2_test()
  firebase_connection = await fb_test()
  return r2_connection and firebase_connection

async def sync_manually_added_memes():
  manually_added_count = 0
  for meme in await list_files():
    if not await exists(meme.key):
      meme.tags=[Tag.UNTAGGED]
      meme.created_at = meme.updated_at # If meme never existed in firestore, then its last appearence in r2 concidered as creation date
      await save_video_metadata(meme)
      manually_added_count += 1
      print(f"[✔] Detected a new meme\nURL: {meme.url}")

  print(f"\n++++++++++\n🎉Sync completed!\nDetected {manually_added_count} new manually added memes!\n++++++++++\n")