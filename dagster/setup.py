# pylint: disable=missing-module-docstring
from setuptools import find_packages, setup  # pylint: disable=import-error

setup(
    name="repro_dag",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
