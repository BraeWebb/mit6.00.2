import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    lowest = 9999999999
    found = False
    best = []
    for i in range(total, 0, -1):
        if not found:
            for combination in generate_combinations(choices, i, []):
                if len(combination) < lowest:
                    found = True
                    best = combination
                    lowest = len(combination)
    weird_format = choices
    for index, choice in enumerate(choices):
        if choice in best:
            weird_format[index] = 1
        else:
            weird_format[index] = 0
    return weird_format


def generate_combinations(choices, total, current):
    if sum(current) == total:
        yield current
    elif sum(current) > total:
        return
    for index, choice in enumerate(choices):
        left = choices[index+1:]
        yield from generate_combinations(left, total, current + [choice])

print(find_combination([1, 2, 2, 3], 4))
print(find_combination([1, 1, 3, 5, 3], 5))
print(find_combination([1, 1, 1, 9], 4))
print(find_combination([4, 6, 3, 5, 2], 10))