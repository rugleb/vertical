from http import HTTPStatus
from typing import Any, Dict

import orjson
from starlette.responses import JSONResponse, Response

__all__ = (
    "create_response",
    "ok",
    "bad_request",
    "unsupported_media_type",
    "validation_error",
    "server_error",
)


class ORJSONResponse(JSONResponse):

    def render(self, content: Any) -> bytes:
        return orjson.dumps(content)


def create_response(content: Dict, http_status: int) -> Response:
    return ORJSONResponse(content, http_status)


def ok(data: Dict = None, message: str = None) -> Response:  # 200
    content = {
        "data": data or {},
        "message": message or "OK",
    }
    return create_response(content, HTTPStatus.OK)


def bad_request(message: str) -> Response:  # 400
    content = {
        "message": message,
    }
    return create_response(content, HTTPStatus.BAD_REQUEST)


def unsupported_media_type() -> Response:  # 415
    content = {
        "message": "Unsupported media type",
    }
    return create_response(content, HTTPStatus.UNSUPPORTED_MEDIA_TYPE)


def validation_error(errors: Any) -> Response:  # 422
    content = {
        "errors": errors,
        "message": "Input payload validation failed",
    }
    return create_response(content, HTTPStatus.UNPROCESSABLE_ENTITY)


def server_error() -> Response:  # 500
    content = {
        "message": "Internal server error",
    }
    return create_response(content, HTTPStatus.INTERNAL_SERVER_ERROR)
