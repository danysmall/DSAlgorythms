def shell_sort(data: list, reversed: bool = False) -> list:
    """Sort list using Shell algorythm.

    Arguments:
    data — list of data to sort.
    reversed — default False. Set True if you want sort in decending format.
    """
    list_len = len(data)
    if list_len > 2:

        right = shell_sort(data[:list_len // 2])
        left = shell_sort(data[list_len // 2:])

        return _union_two(left, right)

    if list_len == 2:
        if not reversed:
            return [data[1], data[0]] if data[0] > data[1] else data
        return [data[1], data[0]] if data[0] < data[1] else data

    return [data[0]] if list_len == 1 else list()


def _union_two(left: list, right: list) -> list:
    l_len = len(left)
    r_len = len(right)
    if l_len == 0:
        return right
    elif r_len == 0:
        return left
    l_index = 0
    r_index = 0
    result = list()
    while l_index < l_len and r_index < r_len:
        if right[r_index] < left[l_index]:
            result.append(right[r_index])
            r_index += 1
        else:
            result.append(left[l_index])
            l_index += 1

    if l_index >= l_len:
        while r_index < r_len:
            result.append(right[r_index])
            r_index += 1
    else:
        while l_index < l_len:
            result.append(left[l_index])
            l_index += 1

    return result
