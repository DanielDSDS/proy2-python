from typing import  List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from repository.repo_store import StoreRepository

from model.store_model import Song, SongDetails, Singer, Album 

from database import get_db

router = APIRouter()

"""
  En este modulo se definen las rutas correspondientes a cada endpoint
"""

"""
  Endpoint que retorna la lista total de artistas
"""
@router.get('/singers/', response_model=List[Singer], status_code=status.HTTP_200_OK)
async def get_all_singers(db: Session = Depends(get_db)):
  store_repo = StoreRepository()
  return await store_repo.get_all_singers(db = db)

"""
  Endpoint que retorna la lista de canciones del album de un artista 
"""
@router.get('/singers/{id}', response_model=List[Album], status_code=status.HTTP_200_OK)
async def get_albums_by_singer(id: int, db: Session = Depends(get_db)):
  store_repo = StoreRepository()
  return await store_repo.get_albums_by_singer( singer_id = id, db = db)

"""
  Endpoint que retorna la lista de canciones del album un artista 
"""
@router.get('/albums/{id}', response_model=List[Song], status_code=status.HTTP_200_OK)
async def get_songs_by_album(id: int, db: Session = Depends(get_db)):
  store_repo = StoreRepository()
  return await store_repo.get_songs_by_album( album_id = id, db = db)

"""
  Endpoint que retorna la lista total de canciones de un artista 
"""
@router.get('/singer/{id}', response_model=List[Song], status_code=status.HTTP_200_OK)
async def get_songs_by_singer(id: int, db: Session = Depends(get_db)):
  store_repo = StoreRepository()
  return await store_repo.get_songs_by_singer( singer_id = id, db = db)

"""
  Endpoint que retorna los detalles de una canción 
"""
@router.get('/song/{id}', response_model= SongDetails, status_code=status.HTTP_200_OK)
async def get_song_by_id(id: int, db: Session = Depends(get_db)):
  store_repo = StoreRepository()
  return await store_repo.get_song_by_id( id = id, db = db)
