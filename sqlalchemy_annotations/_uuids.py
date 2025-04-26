from typing import Annotated, TypeAlias
from uuid import UUID, uuid4

from sqlalchemy import Uuid
from sqlalchemy.orm import mapped_column

UUIDColumn: TypeAlias = Annotated[UUID, mapped_column(Uuid(), default=uuid4)]
UUIDPKColumn: TypeAlias = Annotated[UUID, mapped_column(Uuid(), primary_key=True, default=uuid4)]
UUIDIndexColumn: TypeAlias = Annotated[UUID, mapped_column(Uuid(), index=True, default=uuid4)]
