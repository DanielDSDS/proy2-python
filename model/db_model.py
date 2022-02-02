from datetime import datetime
from typing import Optional, Text
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from database import Base 

"""
  En este modulo se definen las estructuras de los modelos 
  de acuerdo a las tablas de la base de datos
"""

class Albums(Base):
    __tablename__ = "albums"

    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("artists.ArtistId"))

class Singers(Base):
    __tablename__ = "artists"

    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

class Songs(Base):
    __tablename__ = "tracks"

    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("albums.AlbumId"))
    MediaTypeId = Column(Integer, ForeignKey("media_types.MediaTypeId"))
    GenreId = Column(Integer, ForeignKey("genres.GenreId"))
    Composer = Column(String)
    Milliseconds = Column(Integer)
    Bytes = Column(Integer)
    UnitPrice = Column(Numeric(10, 2))

class Genres(Base):
    __tablename__ = "genres"

    GenreId = Column(Integer, primary_key=True)
    Name = Column(String)

class MediaTypes(Base):
    __tablename__ = "media_types"

    MediaTypeId = Column(Integer, primary_key=True)
    Name = Column(String)