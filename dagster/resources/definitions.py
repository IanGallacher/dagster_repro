# pylint: disable=missing-module-docstring
# pylint: disable-next=import-error
from dagster import Definitions, load_assets_from_modules

from . import assets

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
)
