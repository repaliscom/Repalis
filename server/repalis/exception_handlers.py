from typing import overload
from urllib.parse import urlencode

from fastapi import FastAPI, Request, WebSocket
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.requests import HTTPConnection
from fastapi.responses import JSONResponse, RedirectResponse

from repalis.config import settings
from repalis.exceptions import (
    RepalisError,
    RepalisRedirectionError,
    RepalisRequestValidationError,
)


@overload
async def repalis_exception_handler(
    connection: Request, exc: Exception
) -> JSONResponse: ...


@overload
async def repalis_exception_handler(connection: WebSocket, exc: Exception) -> None: ...


@overload
async def repalis_exception_handler(
    connection: HTTPConnection, exc: Exception
) -> JSONResponse | None: ...


async def repalis_exception_handler(
    connection: HTTPConnection, exc: Exception
) -> JSONResponse | None:
    assert isinstance(exc, RepalisError)
    response = JSONResponse(
        status_code=exc.status_code,
        content={"error": type(exc).__name__, "detail": jsonable_encoder(exc.detail)},
        headers=exc.headers,
    )
    if isinstance(connection, WebSocket):
        await connection.send_denial_response(response)
        return None
    return response


async def request_validation_exception_handler(
    request: Request, exc: Exception
) -> JSONResponse:
    assert isinstance(exc, (RequestValidationError, RepalisRequestValidationError))
    return JSONResponse(
        status_code=422,
        content={
            "error": type(exc).__name__,
            "detail": jsonable_encoder(
                exc.errors(),
                custom_encoder={bytes: _encode_bytes_safely},
            ),
        },
    )


def _encode_bytes_safely(value: bytes) -> str:
    return value.decode("utf-8", errors="replace")


async def polar_redirection_exception_handler(
    request: Request, exc: Exception
) -> RedirectResponse:
    assert isinstance(exc, RepalisRedirectionError)
    error_url_params = urlencode(
        {
            "message": exc.message,
            "return_to": exc.return_to or settings.FRONTEND_DEFAULT_RETURN_PATH,
        }
    )
    error_url = f"{settings.generate_frontend_url('/error')}?{error_url_params}"
    return RedirectResponse(error_url, exc.status_code)


def add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        RepalisRedirectionError, polar_redirection_exception_handler
    )

    app.add_exception_handler(
        RequestValidationError, request_validation_exception_handler
    )
    app.add_exception_handler(
        RepalisRequestValidationError, request_validation_exception_handler
    )
    app.add_exception_handler(RepalisError, repalis_exception_handler)
