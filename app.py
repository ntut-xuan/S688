import json
from typing import Any

from loguru import logger

from loader import ComponentType, load_swagger_component, load_swagger_file
from flator import flat


if __name__ == "__main__":
    swagger_data: dict[str, Any] = load_swagger_file("swagger.json")
    schema_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.SCHEMA)
    response_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.RESPONSE)
    swagger_flat_data = flat(swagger_data, schema_components, response_components)