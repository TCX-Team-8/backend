from fastapi import FastAPI
from .routes.user import user_router
from .routes.conge import conge_router
from .routes.seuil import seuil_router
from .routes.pointage import pointage_router
from .routes.auth import router as auth_router

app = FastAPI()
app.include_router(user_router, prefix="/utilisateurs", tags=["utilisateurs"])
app.include_router(conge_router, prefix="/conge", tags=["conge"])
app.include_router(seuil_router, prefix="/seuil", tags=["seuil"])
app.include_router(pointage_router, prefix="/pointage", tags=["pointage"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])