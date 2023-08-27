import json
import sys
from dataclasses import dataclass
from http import HTTPMethod
from typing import Any

from loguru import logger

from loader import ComponentType, load_swagger_component, load_swagger_file
from flator import flat

@dataclass
class Route:
    method: HTTPMethod
    path: str
    request_payload: dict[str, Any] | None = None
    response_payload: dict[str, Any] | None = None


def fetch_route(swagger_flat_data: dict[str, Any]):
    paths: dict[str, dict[str, Any]] = swagger_flat_data["paths"]
    routes: list[Route] = []

    for path_name, path_object in paths.items():
        for key, value in path_object.items():
            logger.debug(f"Fetch route {key.upper():8s} {path_name}")
            routes.append(Route(method=HTTPMethod(key.upper()), path=path_name))
    logger.info(f"Fetch {len(routes)} routes.")


def setup_loguru_format() -> None:
    logger.remove()
    logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> [<level>{level:^7s} </level>] - <level>{message}</level>")

if __name__ == "__main__":

    setup_loguru_format()

    swagger_data: dict[str, Any] = load_swagger_file("swagger.json")
    schema_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.SCHEMA)
    response_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.RESPONSE)
    swagger_flat_data = flat(swagger_data, schema_components, response_components)

    fetch_route(swagger_flat_data)