from fastapi import FastAPI

from app.router.user import User

app = FastAPI()
User(app=app)
