from fastapi import APIRouter, Depends
from fastapi_cache.decorator import cache
from pydantic import BaseModel

from app.dependencies import get_token_header
from app.handler.short_url import ShortURL

router = APIRouter(
    prefix="/v1",
    tags=["API"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@cache()
async def get_cache():
    return 1


class SchemaShortURL(BaseModel):
    url: str


@router.get("/short-url")
@cache(expire=20)
async def read_users():
    return await ShortURL().get()


@router.post("/short-url")
@cache(expire=2)
async def read_user(item: SchemaShortURL):
    return await ShortURL().post(item)
