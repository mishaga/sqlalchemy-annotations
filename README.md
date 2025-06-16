# Table column annotations for SQLAlchemy

> Table column annotations for [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)

Instead of this:

```python
from datetime import UTC, datetime
from uuid import UUID, uuid4

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    id: Mapped[int] = mapped_column(sa.Integer(), sa.Identity(always=True), primary_key=True)
    email: Mapped[str] = mapped_column(sa.Text(), unique=True, default='')
    confirmed: Mapped[bool] = mapped_column(sa.Boolean(), default=False)
    connection_id: Mapped[int | None] = mapped_column(sa.BigInteger(), index=True)
    token: Mapped[UUID | None] = mapped_column(sa.Uuid(), index=True, default=uuid4)
    created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), default=lambda: datetime.now(tz=UTC))
```

you can declare your SQLAlchemy models like so:

```python
import sqlalchemy_annotations as saa
from sqlalchemy.orm import Mapped


class User(Base):
    id: Mapped[saa.IntegerPKColumn]
    email: Mapped[saa.TextUniqueColumn]
    confirmed: Mapped[saa.BooleanDefaultFalseColumn]
    connection_id: Mapped[saa.BigIntegerIndexColumn | None]
    token: Mapped[saa.UUIDIndexColumn | None]
    created_at: Mapped[saa.DateTimeDefaultUtcNowColumn]
```

What are these `IntegerPKColumn`, `BigIntegerIndexColumn`, `BooleanDefaultFalseColumn` and other ones?  
These are just type aliases created with `typing.Annotated` function that adds context-specific metadata to a type,
so that you don't need to specify all these extra assignments to `mapped_column` function

## Links

* [Homepage](https://github.com/mishaga/sqlalchemy-annotations)
* [Issues](https://github.com/mishaga/sqlalchemy-annotations/issues)
* [PYPI](https://pypi.org/project/sqlalchemy-annotations/)

## Examples

### Integers (INTEGER, BIGINT, SERIAL, BIGSERIAL)

* `IntegerPKColumn` / `BigIntegerPKColumn` – `INTEGER / BIGINT, GENERATED ALWAYS AS IDENTITY, PRIMARY KEY`
* `SerialPKColumn` / `BigSerialPKColumn` – `SERIAL / BIGSERIAL, PRIMARY KEY`
* `IntegerColumn` / `BigIntegerColumn` – `INTEGER / BIGINT`
* `IntegerIndexColumn` / `BigIntegerIndexColumn` – `INTEGER / BIGINT, INDEX`

```python
from sqlalchemy.orm import Mapped
from sqlalchemy_annotations import IntegerColumn, IntegerIndexColumn, IntegerPKColumn


class Model(Base):
    id: Mapped[IntegerPKColumn]
    # equivalent to
    # id: Mapped[int] = mapped_column(sa.Integer(), Identity(always=True), primary_key=True)

    number: Mapped[IntegerColumn]
    # equivalent to
    # number: Mapped[int] = mapped_column(sa.Integer())

    uid: Mapped[IntegerIndexColumn]
    # equivalent to
    # uid: Mapped[int] = mapped_column(sa.Integer(), index=True)
```

### Strings (TEXT)

* `TextPKColumn` – `TEXT, PRIMARY KEY`
* `TextColumn` – `TEXT` with `default=''`
* `TextUniqueColumn` – `TEXT, UNIQUE`
* `TextIndexColumn` – `TEXT, INDEX`

```python
from sqlalchemy.orm import Mapped
from sqlalchemy_annotations import TextColumn, TextIndexColumn, TextPKColumn, TextUniqueColumn


class Model(Base):
    id: Mapped[TextPKColumn]
    # equivalent to
    # id: Mapped[str] = mapped_column(sa.Text(), primary_key=True)

    name: Mapped[TextColumn]
    # equivalent to
    # name: Mapped[str] = mapped_column(sa.Text(), default='')

    email: Mapped[TextUniqueColumn]
    # equivalent to
    # email: Mapped[str] = mapped_column(sa.Text(), unique=True)

    ext_id: Mapped[TextIndexColumn]
    # equivalent to
    # ext_id: Mapped[str] = mapped_column(sa.Text(), index=True)
```

### UUID (UUID)

* `UUIDPKColumn` – `UUID, PRIMARY KEY` with `default=uuid4`
* `UUIDIndexColumn` – `UUID, INDEX` with `default=uuid4`
* `UUIDColumn` – `UUID` with `default=uuid4`

```python
from sqlalchemy.orm import Mapped
from sqlalchemy_annotations import UUIDColumn, UUIDIndexColumn, UUIDPKColumn


class Model(Base):
    id: Mapped[UUIDPKColumn]
    # equivalent to
    # id: Mapped[str] = mapped_column(sa.Uuid(), primary_key=True, default=uuid4)

    token: Mapped[UUIDIndexColumn]
    # equivalent to
    # token: Mapped[str] = mapped_column(sa.Uuid(), index=True, default=uuid4)

    ext_id: Mapped[UUIDColumn]
    # equivalent to
    # ext_id: Mapped[str] = mapped_column(sa.Uuid(), default=uuid4)
```

### Date, Time, Datetime (DATE, TIME, TIMESTAMP)

* `DateColumn` – `DATE`
* `TimeColumn` – `TIME WITH TIME ZONE`
* `TimeWOTimezoneColumn` – `TIME WITHOUT TIME ZONE`
* `DateTimeColumn` – `TIMESTAMP WITH TIME ZONE`
* `DateTimeWOTimezoneColumn` – `TIMESTAMP WITHOUT TIME ZONE`
* `DateTimeDefaultUtcNowColumn` – `TIMESTAMP WITH TIME ZONE` with `default=lambda: datetime.now(tz=UTC)`

```python
from sqlalchemy.orm import Mapped
from sqlalchemy_annotations import (
    DateColumn,
    DateTimeColumn,
    DateTimeDefaultUtcNowColumn,
    DateTimeWOTimezoneColumn,
    TimeColumn,
    TimeWOTimezoneColumn,
)

class Model(Base):
    ...

    birthday: Mapped[DateColumn]
    # equivalent to
    # birthday: Mapped[date] = mapped_column(sa.Date())

    start_at: Mapped[TimeColumn]
    # equivalent to
    # start_at: Mapped[time] = mapped_column(sa.Time(timezone=True))

    notify_at: Mapped[TimeWOTimezoneColumn]
    # equivalent to
    # notify_at: Mapped[time] = mapped_column(sa.Time(timezone=False))

    approved_at: Mapped[DateTimeColumn]
    # equivalent to
    # approved_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True))

    failed_at: Mapped[DateTimeWOTimezoneColumn]
    # equivalent to
    # failed_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=False))

    created_at: Mapped[DateTimeDefaultUtcNowColumn]
    # equivalent to
    # created_at: Mapped[datetime] = mapped_column(sa.DateTime(timezone=True), default=lambda: datetime.now(tz=UTC))
```

### Booleans (BOOLEAN)

* `BooleanColumn` – `BOOLEAN`
* `BooleanDefaultFalseColumn` – `BOOLEAN` with `default=False`
* `BooleanDefaultTrueColumn` – `BOOLEAN` with `default=True`

```python
from sqlalchemy.orm import Mapped
from sqlalchemy_annotations import BooleanColumn, BooleanDefaultFalseColumn, BooleanDefaultTrueColumn


class Model(Base):
    ...

    is_active: Mapped[BooleanColumn]
    # equivalent to
    # is_active: Mapped[bool] = mapped_column(Boolean())

    is_confirmed: Mapped[BooleanDefaultFalseColumn]
    # equivalent to
    # is_confirmed: Mapped[bool] = mapped_column(Boolean(), default=False)

    is_visible: Mapped[BooleanDefaultTrueColumn]
    # equivalent to
    # is_visible: Mapped[bool] = mapped_column(Boolean(), default=True)
```


### String enums (VARCHAR)

This annotation will not create a native enum  
The column will be `VARCHAR` (without length limit) so that you can easily update your enum

* `BooleanColumn` – `BOOLEAN`
* `BooleanDefaultFalseColumn` – `BOOLEAN` with `default=False`
* `BooleanDefaultTrueColumn` – `BOOLEAN` with `default=True`

```python
from enum import StrEnum

from sqlalchemy.orm import Mapped
from sqlalchemy_annotations import StrEnumColumn


class UserStatus(StrEnum):
    REGISTERED = 'REGISTERED'
    ACTIVATED = 'ACTIVATED'
    BANNED = 'BANNED'


class Model(Base):
    ...

    status: Mapped[StrEnumColumn[UserStatus]]
    # equivalent to
    # status: Mapped[UserStatus] = mapped_column(Enum(UserStatus, native_enum=False, length=None))
```

## A note on contribution

This is opensource project  
So if you find something that you can add of fix, feel free to
open an [issue](https://github.com/mishaga/sqlalchemy-annotations/issues)
and raise a [pull request](https://github.com/mishaga/sqlalchemy-annotations/pulls)

Thank you!
