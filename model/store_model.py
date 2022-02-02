from typing import Optional 
from pydantic import BaseModel

"""
  En este modulo se definen los modelos correspondiente a la salida de cada endpoint
"""

class Song(BaseModel):
    TrackId: int
    Name: str
    AlbumId:  int
    MediaTypeId: int
    GenreId: int
    Composer: Optional[str]
    Milliseconds: int
    Bytes: Optional[int]
    UnitPrice: float

    class Config:
        orm_mode = True

class SongDetails(Song):
    Genre: str
    MediaTypeName: str

    class Config:
        orm_mode = True

class Singer(BaseModel):
    ArtistId: int
    Name: Optional[str]

    class Config:
        orm_mode = True

class Album(BaseModel):
    AlbumId: int
    Title: str
    ArtistId: int

    class Config:
        orm_mode = True