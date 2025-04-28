from typing import Any, TypeAlias

import pytest
from sqlalchemy.orm import MappedColumn

from tests.annotations import CheckAnnotationFn

FIELDS_TO_CHECK = (
    'index',
    'primary_key',
    'unique',
    # 'default',
    'doc',
    'key',
    'info',
    'nullable',
    'onupdate',
    'server_default',
    'server_onupdate',
    # 'type',
    'system',
    'name',
    'autoincrement',
    'comment',
    '_insert_sentinel',
)


@pytest.fixture(scope='session')
def check_annotation() -> CheckAnnotationFn:
    """Return function that checks annotation."""

    def _check_annotation(
        column: TypeAlias,
        expected_type: type,
        expected_column: MappedColumn[Any],
    ) -> None:
        """Check annotation."""
        origin = column.__origin__
        metadata = column.__metadata__

        assert origin == expected_type
        assert len(metadata) == 1

        # assert repr(metadata[0].column) == repr(expected_column.column)
        # meta_col = metadata[0].column
        print()
        print()
        print(type(expected_column))
        print(type(expected_column.column))
        # print(dict(expected_column.column))
        # print(repr(metadata[0]))
        # print(repr(expected_column))
        # print()
        # print(repr(metadata[0].column))
        # print(expected_column.column)
        # print(repr(expected_column.column.column))
        # e = expected_column.column.__clause_element__()
        # print(e)
        # print(type(e))
        # print(repr(e))
        # print()
        # for field in FIELDS_TO_CHECK:
        #     print(field)
        #     assert getattr(metadata[0].column, field) == getattr(expected_column.column, field)
        #     print()
        #     # assert getattr(meta_col, slot) == getattr(expected_column, slot)

    return _check_annotation
