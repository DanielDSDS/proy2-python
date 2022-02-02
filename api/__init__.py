from fastapi import APIRouter
from api.routes import router as music_store_router 

router = APIRouter()

router.include_router(music_store_router, prefix='/api/v1', tags=['Music'])