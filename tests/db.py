from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, declared_attr


class DeclarativeBase:
    """Base class for models."""

    @declared_attr
    def __tablename__(cls) -> str:  # noqa: N805
        """Return table name generated out of class name."""
        return cls.__name__.lower()


Base = declarative_base(cls=DeclarativeBase)
engine = create_engine(
    'sqlite:///:memory:',
    echo=False,
)
