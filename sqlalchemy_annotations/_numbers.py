from typing import Annotated, TypeAlias

from sqlalchemy import BigInteger, Identity, Integer
from sqlalchemy.orm import mapped_column

SerialPKColumn: TypeAlias = Annotated[int, mapped_column(Integer(), primary_key=True, autoincrement=True)]
BigSerialPKColumn: TypeAlias = Annotated[int, mapped_column(BigInteger(), primary_key=True, autoincrement=True)]

IntegerColumn: TypeAlias = Annotated[int, mapped_column(Integer())]
IntegerPKColumn: TypeAlias = Annotated[int, mapped_column(Integer(), Identity(always=True), primary_key=True)]
IntegerIndexColumn: TypeAlias = Annotated[int, mapped_column(Integer(), index=True)]

BigIntegerColumn: TypeAlias = Annotated[int, mapped_column(BigInteger())]
BigIntegerPKColumn: TypeAlias = Annotated[int, mapped_column(BigInteger(), Identity(always=True), primary_key=True)]
BigIntegerIndexColumn: TypeAlias = Annotated[int, mapped_column(BigInteger(), index=True)]
