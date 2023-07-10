from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
import urllib3
from fastapi_route_logger_middleware import RouteLoggerMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.core.log import logger
from app.core.database import engine
from app.api.api_v1.board import board_model

urllib3.disable_warnings()

board_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title = settings.PROJECT_NAME
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
skip_routes = ['/redoc','/docs','/openapi.json']
app.add_middleware(RouteLoggerMiddleware, logger=logger, skip_routes=skip_routes)

# /api/v1
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

