import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from config import settings
from core.exceptions import register_exception_handlers
from core.logging import setup_logging
from db.session import engine
from middleware import register_middleware
from router import api_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---- startup ----
    setup_logging(settings.DEBUG)
    logger.info("Starting %s (%s)", settings.PROJECT_NAME, settings.ENVIRONMENT)
    # init shared clients here, e.g. app.state.redis = ...
    yield
    # ---- shutdown ----
    await engine.dispose()
    logger.info("Shutdown complete")


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_PREFIX}/openapi.json",
        docs_url=None if settings.ENVIRONMENT == "production" else "/docs",
        redoc_url=None,
        lifespan=lifespan,
    )

    register_middleware(app)
    register_exception_handlers(app)
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)
    return app


app = create_app()