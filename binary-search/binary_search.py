def find(search_list, value):
    if value not in search_list:
        raise ValueError("value not in array")

    min = 0
    max = len(search_list) - 1

    while min <= max:
        mid = (max - min) // 2 + min
        if value < search_list[mid]:
            max = mid - 1

        if value > search_list[mid]:
            min = mid + 1

        if value == search_list[mid]:
            return mid
