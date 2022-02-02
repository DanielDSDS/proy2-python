from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import router as store_router
from database import Base, engine

"""
  -> Se crea la base de datos
  -> Se añade el middleware a utilizar
  -> Se define el prefijo a utilizar para las rutas de la API 
"""

def get_application():
      
  Base.metadata.create_all(bind=engine)

  app = FastAPI(title='API libreria musical', version='1.0.0')

  app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
  )

  app.include_router(store_router, prefix='/music-store')
  return app

app = get_application()