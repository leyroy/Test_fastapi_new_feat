from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from config import settings
from middleware.request_context import RequestContextMiddleware


def register_middleware(app: FastAPI) -> None:
    # Last added = outermost (runs first on the way in)
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(RequestContextMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )