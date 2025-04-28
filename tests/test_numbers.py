from typing import TypeAlias

import pytest
from sqlalchemy import BigInteger, Identity, Integer
from sqlalchemy.orm import MappedColumn, mapped_column

from sqlalchemy_annotations import (
    BigIntegerColumn,
    BigIntegerIndexColumn,
    BigIntegerPKColumn,
    BigSerialPKColumn,
    IntegerColumn,
    IntegerIndexColumn,
    IntegerPKColumn,
    SerialPKColumn,
)
from tests.annotations import CheckAnnotationFn


@pytest.mark.parametrize(
    ('column', 'mapped'),
    [
        (SerialPKColumn, mapped_column(Integer(), primary_key=True, autoincrement=True)),
        (BigSerialPKColumn, mapped_column(BigInteger(), primary_key=True, autoincrement=True)),
        (IntegerColumn, mapped_column(Integer())),
        (IntegerPKColumn, mapped_column(Integer(), Identity(always=True), primary_key=True)),
        (IntegerIndexColumn, mapped_column(Integer(), index=True)),
        (BigIntegerColumn, mapped_column(BigInteger())),
        (BigIntegerPKColumn, mapped_column(BigInteger(), Identity(always=True), primary_key=True)),
        (BigIntegerIndexColumn, mapped_column(BigInteger(), index=True)),
    ],
)
def test_int(check_annotation: CheckAnnotationFn, column: TypeAlias, mapped: MappedColumn[int]) -> None:
    """Check number columns."""
    check_annotation(column, int, mapped)
