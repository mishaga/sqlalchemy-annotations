from typing import Annotated, TypeAlias

from sqlalchemy import Boolean
from sqlalchemy.orm import mapped_column

BooleanColumn: TypeAlias = Annotated[bool, mapped_column(Boolean())]
BooleanDefaultTrueColumn: TypeAlias = Annotated[bool, mapped_column(Boolean(), default=True)]
BooleanDefaultFalseColumn: TypeAlias = Annotated[bool, mapped_column(Boolean(), default=False)]
