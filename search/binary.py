import typing
from collections.abc import Iterable


def binary_search(
    data: Iterable[typing.Any],
    value: typing.Any
) -> typing.Union[None, int]:
    """Fast binart search algorythm.

    Attributes:
    • data — iterable object.
    • value — value that need to find.

    Return:
    • index — if given value is found.
    • None — if given value is not found.
    """
    l_index = 0
    r_index = len(data) - 1

    while l_index <= r_index:
        index = l_index + (r_index - l_index) // 2
        if data[index] < value:
            l_index = index
        elif data[index] > value:
            r_index = index
        elif data[index] == value:
            return index
        else:
            return None
