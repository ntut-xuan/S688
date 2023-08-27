from typing import Any

from loader import ComponentType
from loguru import logger


def flat(swagger_data: dict[str, Any], schemas: dict[str, Any], responses: dict[str, Any]) -> dict[str, Any]:
    _flat_ref_key(swagger_data, schemas, responses)
    logger.info("Flat the Swagger: replace the ref with the components.")
    del swagger_data["components"]

    return swagger_data


def _flat_ref_key(data: dict[str, Any], schemas: dict[str, Any], responses: dict[str, Any]) -> None:
    components: dict[str, Any] = {**schemas, **responses}

    for _, value in data.items():
        if isinstance(value, dict):
            _flat_ref_key(value, schemas, responses)

    if "$ref" in data.keys():
        ref_path: str = data["$ref"]
        ref_json_object: dict[str, Any] = components[ref_path]
        del data["$ref"]
        data |= ref_json_object