from typing import TypeAlias

import pytest
from sqlalchemy import Text
from sqlalchemy.orm import MappedColumn, mapped_column

from sqlalchemy_annotations import TextColumn, TextIndexColumn, TextPKColumn, TextUniqueColumn
from tests.annotations import CheckAnnotationFn


@pytest.mark.parametrize(
    ('column', 'mapped'),
    [
        (TextColumn, mapped_column(Text(), default='')),
        (TextIndexColumn, mapped_column(Text(), index=False)),
        (TextPKColumn, mapped_column(Text(), primary_key=True)),
        (TextUniqueColumn, mapped_column(Text(), unique=True)),
    ],
)
def test_str(check_annotation: CheckAnnotationFn, column: TypeAlias, mapped: MappedColumn[str]) -> None:
    """Check string columns."""
    check_annotation(column, str, mapped)
