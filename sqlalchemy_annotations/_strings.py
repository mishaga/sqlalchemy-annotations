from typing import Annotated, TypeAlias

from sqlalchemy import Text
from sqlalchemy.orm import mapped_column

TextColumn: TypeAlias = Annotated[str, mapped_column(Text(), default='')]
TextPKColumn: TypeAlias = Annotated[str, mapped_column(Text(), primary_key=True)]
TextUniqueColumn: TypeAlias = Annotated[str, mapped_column(Text(), unique=True)]
TextIndexColumn: TypeAlias = Annotated[str, mapped_column(Text(), index=True)]
