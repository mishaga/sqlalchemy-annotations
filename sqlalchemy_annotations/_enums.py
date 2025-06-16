from enum import StrEnum
from typing import Annotated, Generic, TypeVar

from sqlalchemy import Enum
from sqlalchemy.orm import mapped_column

E = TypeVar('E', bound=StrEnum)


class StrEnumColumn(Generic[E]):
    """StrEnumColumn type."""

    def __class_getitem__(cls, enum_type: type[E]) -> Annotated[E, mapped_column(Enum)]:
        """Return annotated type for a StrEnum."""
        return Annotated[enum_type, mapped_column(Enum(enum_type, native_enum=False, length=None))]
