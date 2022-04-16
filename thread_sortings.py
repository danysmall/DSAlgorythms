from multiprocessing import Process, Manager


def hyperthread_shell_sort(data: list) -> list:
    """Should use for arrays more than 400k items."""
    threads_count = 1
    data_len = len(data)
    while data_len > 500000:
        threads_count += 1
        data_len //= 2

    data_len = len(data)
    process_pool = list()
    manager = Manager()
    return_dict = manager.dict()

    left_counter = 0
    right_counter = data_len // threads_count
    step = data_len // threads_count
    for i in range(threads_count - 1):
        process = Process(
            target=_shell_parallel_middleware,
            args=(data[left_counter:right_counter], return_dict, i))
        process_pool.append(process)
        left_counter = right_counter
        right_counter += step

    for process in process_pool:
        process.start()
        process.join()

    return_dict[threads_count - 1] = shell_sort(data[left_counter:])
    return union_all(return_dict.values())


def union_all(data: list) -> list:
    data_len = len(data)
    if data_len > 2:
        return union_two(union_all(data[data_len // 2:]),
                         union_all(data[:data_len // 2]))
    if data_len == 2:
        return union_two(data[0], data[1])

    if data_len == 1:
        return data[0]
    return list()


def union_two(left: list, right: list) -> list:
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


def _shell_parallel_middleware(data: list, return_dict, proc) -> list:
    result = shell_sort(data)
    return_dict[proc] = result


def shell_sort(data: list) -> list:
    list_len = len(data)
    if list_len > 2:

        right = shell_sort(data[:list_len // 2])
        left = shell_sort(data[list_len // 2:])

        return union_two(left, right)

    if list_len == 2:
        return [data[1], data[0]] if data[0] > data[1] else data

    return [data[0]] if list_len == 1 else list()
