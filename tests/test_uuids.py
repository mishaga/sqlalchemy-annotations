from typing import TypeAlias
from uuid import UUID

import pytest
from sqlalchemy import Uuid
from sqlalchemy.orm import MappedColumn, mapped_column

from sqlalchemy_annotations import UUIDColumn, UUIDIndexColumn, UUIDPKColumn
from tests.annotations import CheckAnnotationFn


@pytest.mark.parametrize(
    ('column', 'mapped'),
    [
        (UUIDColumn, mapped_column(Uuid(), default=...)),
        (UUIDIndexColumn, mapped_column(Uuid(), index=True, default=...)),
        (UUIDPKColumn, mapped_column(Uuid(), primary_key=True, default=...)),
    ],
)
def test_uuid(check_annotation: CheckAnnotationFn, column: TypeAlias, mapped: MappedColumn[UUID]) -> None:
    """Check UUID columns."""
    check_annotation(column, UUID, mapped)
