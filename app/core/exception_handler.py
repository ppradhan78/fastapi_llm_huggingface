import logging
from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import AppException

logger = logging.getLogger(__name__)


def register_exception_handlers(app):

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        logger.error(f"Application error: {exc.message}")

        return JSONResponse(
            status_code=400,
            content={
                "error": "Application Error",
                "message": exc.message
            }
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception occurred")

        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal Server Error",
                "message": "Something went wrong"
            }
        )