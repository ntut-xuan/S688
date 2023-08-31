import json
import sys
from dataclasses import dataclass
from http import HTTPMethod
from typing import Any

import click
from loguru import logger

import flator
from loader import ComponentType, load_swagger_component, load_swagger_file
from route import Route, fetch_route


def setup_loguru_format() -> None:
    logger.remove()
    logger.add(sys.stderr, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> [<level>{level:^7s} </level>] - <level>{message}</level>")


@click.command()
@click.argument('swagger_file')
@click.option('--output', '-o', type=click.Path(), help='Output filename for flattened JSON')
def flat(swagger_file, output):
    swagger_data: dict[str, Any] = load_swagger_file(swagger_file)
    schema_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.SCHEMA)
    response_components: dict[str, Any] = load_swagger_component(swagger_data, ComponentType.RESPONSE)
    swagger_flat_data = flator.flat(swagger_data, schema_components, response_components)

    with open(output, 'w') as file:
        file.write(json.dumps(swagger_flat_data))
    logger.info(f"Write the flat result to file {output}")


@click.command()
@click.argument('swagger_file')
def validate(swagger_file):
    pass #TODO: Implement in the future


if __name__ == "__main__":
    setup_loguru_format()

    cli = click.Group()
    cli.add_command(flat)
    cli.add_command(validate)
    cli()