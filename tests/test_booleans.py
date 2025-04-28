from typing import TypeAlias

import pytest
from sqlalchemy import Boolean
from sqlalchemy.orm import MappedColumn, mapped_column

from sqlalchemy_annotations import BooleanColumn, BooleanDefaultFalseColumn, BooleanDefaultTrueColumn
from tests.annotations import CheckAnnotationFn


@pytest.mark.parametrize(
    ('column', 'mapped'),
    [
        (BooleanDefaultTrueColumn, mapped_column(Boolean(), default=True)),
        (BooleanDefaultFalseColumn, mapped_column(Boolean(), default=False)),
        (BooleanColumn, mapped_column(Boolean())),
    ],
)
def test_bool(check_annotation: CheckAnnotationFn, column: TypeAlias, mapped: MappedColumn[bool]) -> None:
    """Check boolean columns."""
    check_annotation(column, bool, mapped)
