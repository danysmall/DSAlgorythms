"""Implemetations of sorting functions."""
import typing
import time


SORT_LIST = [6, 3, 1, 4, 8, 2, 5, 7]

COUNT_BIG_SORT = 300000
BIG_DATA_SORT_LIST = [i for i in range(COUNT_BIG_SORT, 0, -1)]


def insertion_sort(data: list, reverse: bool = False) -> list:
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


def shell_sort(data: list) -> list:
    list_len = len(data)
    if list_len > 3:

        right = shell_sort(data[:list_len // 2])
        left = shell_sort(data[list_len // 2:])

        l_index = 0
        r_index = 0
        result = list()
        while l_index < len(left) and r_index < len(left):
            if right[r_index] < left[l_index]:
                result.append(right[r_index])
                r_index += 1
            else:
                result.append(left[l_index])
                l_index += 1

        if l_index >= len(left):
            while r_index < len(right):
                result.append(right[r_index])
                r_index += 1
        else:
            while l_index < len(left):
                result.append(left[l_index])
                l_index += 1

        return result

    if list_len == 2:
        return [data[1], data[0]] if data[0] > data[1] else data

    if data[0] > data[1]:
        if data[1] > data[2]:
            return [data[2], data[1], data[0]]
        return [data[1], data[2], data[0]]
    else:
        if data[1] < data[2]:
            return [data[0], data[1], data[2]]
        return [data[0], data[2], data[1]]


def linear_search(data: list, value) -> typing.Union[typing.Any, None]:
    for i, val in enumerate(data):
        if val == value:
            return i
    return None


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
    # th1 = ThreadWithReturn(target=ret, args=('hello',))
    # th1.start()
    # th1.join()
    # r = th1.get_result()
    # print(r)
    # test_sortings_speed()

    start = time.time()
    shell_sort(BIG_DATA_SORT_LIST)
    print(time.time() - start)

    # print(f'Insertion sort: {insertion_sort(SORT_LIST)}')
    # print(f'Insertion sort (Reverse): {insertion_sort(SORT_LIST, True)}')
    # print(linear_search(SORT_LIST, 10))
