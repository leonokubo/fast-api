from typing import Union

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.dependencies import get_token_header
from app.handler.short_url import ShortURL

router = APIRouter(
    prefix="/v1",
    tags=["API"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


class SchemaShortURL(BaseModel):
    url: str


@router.get("/short-url")
async def read_users():
    x=1
    return ShortURL.get()


@router.post("/short-url")
async def read_user(item: SchemaShortURL):
    return ShortURL.post(item)
