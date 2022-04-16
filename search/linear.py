import typing


def linear_search(
    data: list,
    value: typing.Any
) -> typing.Union[typing.Any, None]:
    """Linear search in iterable object.

    Arguments:
    • data — iterable object (list).
    • value — value that need to find.

    Return:
    • Return index of value if is found
    • Return None if value is not found
    """
    for i, val in enumerate(data):
        if val == value:
            return i
    return None
