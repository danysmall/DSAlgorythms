"""Bubble sort."""
import typing
from collections.abc import Iterable


def bubble_sort(
    data: Iterable[typing.Any],
    reversed: bool = False
) -> Iterable[typing.Any]:
    """Bubble sort algorythm.

    Attributes:
    • data — iterable object that needed to sort.
    • reversed — set True if need sort in decending order.

    Return:
    • Iterable object (data) sotred.
    """
    data_len = len(data)

    def acending():
        for i in range(data_len):
            for j in range(data_len - i - 1):
                if data[j] > data[j + 1]:
                    data[j + 1], data[j] = data[j], data[j + 1]
        return data

    def decending():
        for i in range(data_len):
            for j in range(data_len - i - 1):
                if data[j] < data[j + 1]:
                    data[j + 1], data[j] = data[j], data[j + 1]
        return data

    return decending() if reversed else acending()

if __name__ == '__main__':
    TEST_DATA = [i for i in range(100, 0, -4)]

    print(f'Dataset: {TEST_DATA}')
    print(f'Acending sort: {bubble_sort(TEST_DATA)}')
    print(f'Decending sort: {bubble_sort(TEST_DATA, reversed=True)}')
