from dataclasses import dataclass
from http import HTTPMethod, HTTPStatus
from typing import Any

from loguru import logger


@dataclass
class Route:
    method: HTTPMethod
    path: str
    request_payload: dict[str, Any] | None = None
    response_payload: dict[int, dict[str, Any]] | None = None


def fetch_route(swagger_flat_data: dict[str, Any]):
    paths: dict[str, dict[str, Any]] = swagger_flat_data["paths"]
    routes: list[Route] = []

    for path_name, path_object in paths.items():
        for key, value in path_object.items():
            logger.debug(f"Fetching route {key.upper():8s} {path_name}")
            route: Route = Route(method=HTTPMethod(key.upper()), path=path_name, request_payload=_fetch_request_body(value), response_payload=_fetch_responses(value))
            routes.append(route)
    logger.info(f"Fetch {len(routes)} routes.")


def _fetch_request_body(route_data: dict[str, Any]):
    if "requestBody" in route_data and "application/json" in route_data["requestBody"]["content"]:
        schema = route_data["requestBody"]["content"]["application/json"]["schema"]
        payload = _generate_payload_from_schema(schema)
        logger.debug(f"Fetch request payload: Skip since it doesn't have application/json schema")
        return payload
    logger.debug(f"Fetch request payload: Ok")
    return None


def _fetch_responses(route_data: dict[str, Any]):
    if "responses" not in route_data:
        return None
    responses: dict[str, Any] = route_data["responses"]
    responses_payload: dict[HTTPStatus, dict[str, Any]] = {}
    for status_code_str, response in responses.items():
        status_code: HTTPStatus = HTTPStatus(int(status_code_str))
        if "content" not in response or "application/json" not in response["content"]:
            responses_payload[status_code] = None
            logger.debug(f"Fetch status code {str(status_code)}: Skip since it doesn't have application/json schema")
            continue
        schema = response["content"]["application/json"]["schema"]
        responses_payload[status_code] = _generate_payload_from_schema(schema)
        logger.debug(f"Fetch status code {str(status_code)}: Ok")
    logger.debug(f"Fetch {len(responses_payload.keys())} status code.")
    return responses_payload


def _generate_payload_from_schema(schema: dict[str, Any]):
    schema_type = schema["type"]

    if schema_type == "object":
        properties_dict: dict[str, Any] = schema["properties"]
        payload: dict[str, Any] = {}
        for key, value in properties_dict.items():
            payload[key] = _generate_payload_from_schema(properties_dict[key])
        return payload
    elif schema_type == "array":
        item: dict[str, Any] = schema["items"]
        payload: list[Any] = [_generate_payload_from_schema(item)]
        return payload
    elif schema_type == "string":
        return schema["example"] if "example" in schema else "string"
    elif schema_type == "integer":
        return schema["example"] if "example" in schema else 0