def read_file(file_path):
    """
    Read from a file called systemparamter.csv
    The file has to be defined as:
    x;y;z
    x1;y1;z1

    Note:
        semicolon (;) seperation
        newline (\n) defines new entry
    """
    with open(file_path, 'r', newline='') as file:
        return list(file.read())


def day_one_part_one():
    data = read_file("input/day1part1")
    last_value = 1
    sum_value = 0
    for index, value_str in enumerate(data):
        value = int(value_str)
        if value == last_value:
            sum_value = sum_value + value
        last_value = value
        if index == len(data) - 1:
            if value_str == data[0]:
                sum_value = sum_value + value
    print("Day 1 part 1:" + str(sum_value))


def day_one_part_two():
    data = read_file("input/day1part1")
    last_value = 1
    sum_value = 0
    half_way_point = int(len(data) / 2)
    for index, value_str in enumerate(data):
        value = int(value_str)
        value_plus_half = int(data[half_way_point + index])
        if value == value_plus_half:
            sum_value = sum_value + value + value_plus_half
        if index == half_way_point-1:
            break
    print("Day 1 part 2:" + str(sum_value))