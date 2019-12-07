import math

from helpers import readfile


def partone(data):
    sum_value = 0
    for x in data:
        sum_value = sum_value + math.floor(x / 3) - 2
    return sum_value


def parttwo(data):
    sum_value = 0
    for x in data:
        internal_count = math.floor(x / 3) - 2
        sum_value = sum_value + internal_count
        while internal_count > 0:
            internal_count = math.floor(internal_count / 3) - 2
            if internal_count > 0:
                sum_value = sum_value + internal_count
    return sum_value


if __name__ == '__main__':
    values = readfile.readcsv('inputs/day01.csv')
    data = []
    for value in values:
        data.append(int(value))
    print(partone(data))
    print(parttwo(data))
