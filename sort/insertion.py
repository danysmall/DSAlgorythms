def insertion_sort(data: list, reverse: bool = False) -> list:
    """Sort list using insertion algorythm.

    Arguments:
    data — list of data to sort.
    reversed — default False. Set True if you want sort in decending format.
    """
    if not reverse:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    else:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] < key:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
    return data
