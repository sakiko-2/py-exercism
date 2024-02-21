def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for item in lists:
        result += item

    return result


def filter(function, list):
    return [item for item in list if function(item)]

    
def length(list):
    count = 0
    for item in list:
        count += 1

    return count


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)

    return initial


def reverse(list): 
    return list[::-1]
