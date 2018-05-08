from flask_app import db
from flask_app import Song
import constants

for song in constants.TOP_TEN_SONGS:
    db.session.add(
        Song(
            title=song.title,
            artist_name=song.artist_name,
            youtube_url=song.youtube_url))

db.session.commit()