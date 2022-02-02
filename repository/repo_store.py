from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import Session

from database import engine

from model.store_model import Song, SongDetails, Singer, Album
from model.db_model import Albums, Singers, Songs, Genres, MediaTypes 

store_db = []

"""
  En este modulo se define una clase con la lógica de negocio a utilizar en los endpoints 
"""

class StoreRepository:
    async def get_all_singers(self, db: Session) -> List[Singer]: 
      """
        Servicio para endpoint music-store/api/v1/singers/ 
        Retorna la lista total de artistas
      """
      singers_list = db.query(Singers).all()

      return singers_list

    async def get_albums_by_singer(self, *, singer_id: int, db: Session) -> List[Album]:
      """
        Servicio para endpoint music-store/api/v1/singers/{id} 
        Retorna la lista de canciones del album de un artista 
      """
      albums = db.query(Albums).filter(Albums.ArtistId == singer_id).all()

      return albums 

    async def get_songs_by_album(self, *, album_id: int, db: Session) -> List[Song]:
      """
        Servicio para endpoint music-store/api/v1/albums/{id} 
        Retorna la lista de canciones del album un artista 
      """
      songs = db.query(Songs).filter(Songs.AlbumId == album_id).all()

      return songs 

    async def get_songs_by_singer(self, *, singer_id: int, db: Session) -> List[Song]:
      """
        Servicio para endpoint music-store/api/v1/singer/{id} 
          Retorna la lista total de canciones de un artista 
      """
      songs = []
      singer_albums = db.query(Albums).filter(Albums.ArtistId == singer_id).all()

      for album in singer_albums:
        songs.extend(db.query(Songs).filter(Songs.AlbumId == album.AlbumId).all())

      return songs 

    async def get_song_by_id(self, *, id: int, db: Session) -> SongDetails:
      """
        Servicio para endpoint music-store/api/v1/song/{id} 
          Retorna los detalles de una canción 
      """
      song = db.query(Songs).get(id)
      song_genre = db.query(Genres).get(song.GenreId)
      song_media_type = db.query(MediaTypes).get(song.MediaTypeId)

      return {**song.__dict__, "Genre": song_genre.Name, "MediaTypeName": song_media_type.Name}