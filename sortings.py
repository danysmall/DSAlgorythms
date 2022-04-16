"""Implemetations of sorting functions."""
import time
from sort import shell_sort, insertion_sort
from search import linear_search, binary_search


SORT_LIST = [6, 3, 1, 4, 8, 2, 5, 7, 9]

COUNT_BIG_SORT = 5000
BIG_DATA_SORT_LIST = [i for i in range(COUNT_BIG_SORT, 0, -1)]


def test_sortings_speed(step: int = 1000):
    for i in range(step, step * 11, step):
        print(f'Test for {i} values')

        start = time.time()
        result_s = shell_sort([j for j in range(i, 0, -1)])
        elapsed_time = time.time() - start
        is_correct = check_for_correct(result_s)
        print(f'Shell sort: {elapsed_time} -> {is_correct}')

        start = time.time()
        result_i = insertion_sort([j for j in range(i, 0, -1)])
        elapsed_time = time.time() - start
        is_correct = check_for_correct(result_i)
        print(f'insertion_sort {elapsed_time} -> {is_correct}')

        print(f'Shell list == Insertion list -> {result_s == result_i}')

        print('-' * 40)


def check_for_correct(data: list) -> bool:
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


if __name__ == '__main__':
    print(f'Start data: {SORT_LIST}')

    start = time.time()
    shell_sort(BIG_DATA_SORT_LIST)
    print(time.time() - start)

    print(f'Insertion sort: {insertion_sort(SORT_LIST)}')
    print(binary_search(SORT_LIST, 7))
    print(f'Insertion sort (Reverse): {insertion_sort(SORT_LIST, True)}')
    print(linear_search(SORT_LIST, 7))
