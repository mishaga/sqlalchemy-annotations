from collections.abc import Callable
from typing import Any

from sqlalchemy.orm import MappedColumn

CheckAnnotationFn = Callable[[type, type, MappedColumn[Any]], None]
