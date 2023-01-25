from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from routers import passes
from database.models import Base
from database.database import engine


Base.metadata.create_all(bind=engine)

api = FastAPI()

api.include_router(passes.router)


@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse({"status": 422, "message": str(exc)[:200], "id": "None"}, status_code=422)


@api.exception_handler(Exception)
async def exception_callback(request: Request, exc: Exception):
    return JSONResponse({"status": 500, "message": str(exc)[:200], "id": "None"}, status_code=500)
