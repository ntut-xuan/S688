import json
import sys
from dataclasses import dataclass
from http import HTTPMethod
from typing import Any

from loguru import logger

from flator import flat
from loader import ComponentType, load_swagger_component, load_swagger_file
from route import Route, fetch_route


def setup_loguru_format() -> None:
    logger.remove()
    logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> [<level>{level:^7s} </level>] - <level>{message}</level>")

if __name__ == "__main__":

    setup_loguru_format()

    swagger_data: dict[str, Any] = load_swagger_file("swagger.json")
    schema_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.SCHEMA)
    response_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.RESPONSE)
    swagger_flat_data = flat(swagger_data, schema_components, response_components)

    route: Route = fetch_route(swagger_flat_data)