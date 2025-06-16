from sqlalchemy.orm import Mapped
from sqlalchemy.sql.ddl import CreateTable

from sqlalchemy_annotations import BooleanColumn, BooleanDefaultFalseColumn, BooleanDefaultTrueColumn, SerialPKColumn
from tests.db import Base, engine


def clean_multiline(sql: str) -> str:
    """Strip each line of a multiline string."""
    lines = (line.strip() for line in sql.split('\n'))
    return '\n'.join(line for line in lines if line != '')


def test_bool_not_null() -> None:
    """Check boolean columns not null."""

    class B1(Base):
        id: Mapped[SerialPKColumn]
        bool_true: Mapped[BooleanDefaultTrueColumn]
        bool_false: Mapped[BooleanDefaultFalseColumn]
        bool_no_default: Mapped[BooleanColumn]

    sql = CreateTable(B1.__table__).compile(engine)
    expected = [
        'CREATE TABLE b1 (',
        'id INTEGER NOT NULL,',
        'bool_true BOOLEAN NOT NULL,',
        'bool_false BOOLEAN NOT NULL,',
        'bool_no_default BOOLEAN NOT NULL,',
        'PRIMARY KEY (id)',
        ')',
    ]
    assert clean_multiline(str(sql)) == '\n'.join(expected)


def test_bool_with_null() -> None:
    """Check boolean columns with nulls."""

    class B2(Base):
        id: Mapped[SerialPKColumn]
        bool_true: Mapped[BooleanDefaultTrueColumn | None]
        bool_false: Mapped[BooleanDefaultFalseColumn | None]
        bool_no_default: Mapped[BooleanColumn | None]

    sql = CreateTable(B2.__table__).compile(engine)
    expected = [
        'CREATE TABLE b2 (',
        'id INTEGER NOT NULL,',
        'bool_true BOOLEAN,',
        'bool_false BOOLEAN,',
        'bool_no_default BOOLEAN,',
        'PRIMARY KEY (id)',
        ')',
    ]
    assert clean_multiline(str(sql)) == '\n'.join(expected)
