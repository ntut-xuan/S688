import json
from typing import Any
from enum import Enum

from loguru import logger


class ComponentType(Enum):
    SCHEMA: str = "schemas"
    RESPONSE: str = "responses"


def load_swagger_file(filename: str) -> dict[str, Any]:
    swagger_text: str = ""
    
    with open(filename, "r") as f:
        swagger_text = f.read()

    logger.info(f"Load Swagger file: {filename}")
    return json.loads(swagger_text)


def load_swagger_component(swagger_data: dict[str, Any], component_type: ComponentType):
    schema_component_dict: dict[str, Any] = {}
    component_type_string: str = component_type.value

    if ("components" not in swagger_data) or (component_type_string not in swagger_data["components"]):
        logger.info(f"Load Swagger schema component: Skip due to the file doesn't have {component_type_string} component.")
        return schema_component_dict
    
    schemas_data: dict[str, Any] = swagger_data["components"][component_type_string]

    if (type(schemas_data) is not dict):
        logger.info(f"Load Swagger schema component: Skip due to the schemas components is not the json object.")
        return schema_component_dict

    for component_name, value in swagger_data["components"][component_type_string].items():
        schema_component_dict |= {f'#/components/{component_type_string}/{component_name}': value}
        logger.debug(f"Load Swagger {component_type_string} component: #/components/{component_type_string}/{component_name}")

    logger.info(f"Load {len(schema_component_dict.keys())} {component_type_string} components")
    return schema_component_dict