# data_utils.py

from collections import Counter

def mean(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n // 2]
    else:
        middle1, middle2 = numbers[n // 2 - 1], numbers[n // 2]
        return (middle1 + middle2) / 2

def mode(numbers):
    if len(numbers) == 0:
        return None
    count = Counter(numbers)
    mode_value, _ = count.most_common(1)[0]
    return mode_value
