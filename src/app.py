from fastadmin import fastapi_app as admin_app
from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import JSONResponse

from src.utils.exceptions import (
    ResultNotFound,
    WrongCredentials,
    ForeignKeyError
)


app = FastAPI(
    title="auto_service backend",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/admin", admin_app, "admin panel")

main_app_router = APIRouter(prefix="/api")


@app.exception_handler(ResultNotFound)
async def result_not_found(
    request: Request, exc: ResultNotFound
):
    return JSONResponse(status_code=404, content={})


@app.exception_handler(WrongCredentials)
async def wrong_credentials(
    request: Request, exc: WrongCredentials
):
    return JSONResponse(status_code=401, content={})


@app.exception_handler(ForeignKeyError)
async def foreign_key_error(
    request: Request, exc: ForeignKeyError
):
    return JSONResponse(status_code=400, content={})
