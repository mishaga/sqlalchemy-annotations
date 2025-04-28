from datetime import date, datetime, time
from typing import TypeAlias

import pytest
from sqlalchemy import Date, DateTime, Time
from sqlalchemy.orm import MappedColumn, mapped_column

from sqlalchemy_annotations import (
    DateColumn,
    DateTimeColumn,
    DateTimeDefaultUtcNowColumn,
    DateTimeWOTimezoneColumn,
    TimeColumn,
    TimeWOTimezoneColumn,
)
from tests.annotations import CheckAnnotationFn


@pytest.mark.parametrize(
    ('column', 'mapped'),
    [
        (DateColumn, mapped_column(Date())),
    ],
)
def test_date(check_annotation: CheckAnnotationFn, column: TypeAlias, mapped: MappedColumn[date]) -> None:
    """Check date columns."""
    check_annotation(column, date, mapped)


@pytest.mark.parametrize(
    ('column', 'mapped'),
    [
        (TimeColumn, mapped_column(Time(timezone=True))),
        (TimeWOTimezoneColumn, mapped_column(Time(timezone=False))),
    ],
)
def test_time(check_annotation: CheckAnnotationFn, column: TypeAlias, mapped: MappedColumn[time]) -> None:
    """Check time columns."""
    check_annotation(column, time, mapped)


@pytest.mark.parametrize(
    ('column', 'mapped'),
    [
        (DateTimeColumn, mapped_column(DateTime(timezone=True))),
        (DateTimeDefaultUtcNowColumn, mapped_column(DateTime(timezone=True), default=...)),
        (DateTimeWOTimezoneColumn, mapped_column(DateTime(timezone=False))),
    ],
)
def test_datetime(check_annotation: CheckAnnotationFn, column: TypeAlias, mapped: MappedColumn[datetime]) -> None:
    """Check datetime columns."""
    check_annotation(column, datetime, mapped)
