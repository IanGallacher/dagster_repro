from dagster import (
    StaticPartitionsDefinition,
    graph_asset,
    op,
)

partitions = StaticPartitionsDefinition(["https://www.example.com", "2", "3"])


@op
def op_1():
    return 1


@op
def op_2(number: int):
    return number * 2


@graph_asset(
    partitions_def=partitions,
)
def test_script():
    return op_2(op_1())