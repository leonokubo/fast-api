from fastapi import FastAPI
from pydantic import BaseModel


class Router(BaseModel):
    app: FastAPI


class User(Router):

    @self.app.get("/")
    async def root(self):
        return {"message": "Hello World"}
