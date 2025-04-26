from datetime import UTC, date, datetime, time
from typing import Annotated, TypeAlias

from sqlalchemy import Date, DateTime, Time
from sqlalchemy.orm import mapped_column

DateColumn: TypeAlias = Annotated[date, mapped_column(Date())]

TimeColumn: TypeAlias = Annotated[time, mapped_column(Time(timezone=True))]
TimeWOTimezoneColumn: TypeAlias = Annotated[time, mapped_column(Time(timezone=False))]

DateTimeColumn: TypeAlias = Annotated[datetime, mapped_column(DateTime(timezone=True))]
DateTimeWOTimezoneColumn: TypeAlias = Annotated[datetime, mapped_column(DateTime(timezone=False))]
DateTimeDefaultUtcNowColumn: TypeAlias = Annotated[
    datetime,
    mapped_column(DateTime(timezone=True), default=lambda: datetime.now(tz=UTC)),
]
