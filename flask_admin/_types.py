from collections.abc import Sequence
from typing import Any
from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

if TYPE_CHECKING:
    import sqlalchemy  # noqa

T_COLUMN = Union[str, "sqlalchemy.Column"]
T_FILTER = tuple[int, T_COLUMN, str]
T_COLUMN_LIST = Sequence[T_COLUMN]
T_FORMATTER = Callable[[Any, Any, Any], Any]
T_FORMATTERS = dict[type, T_FORMATTER]
T_STRING_FORMATTERS = dict[Union[str, type], T_FORMATTER]
