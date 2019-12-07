import csv


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
    data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file, delimiter=';', quotechar='|')
        for row in reader:
            data.append(row)
    return data


def day_two_part_one():
    data = read_file("input/day2part1")
    checksum = 0

    for row in data:
        largest_digit = 0
        smallest_digit = 0
        for digit_str in row:
            digit = int(digit_str)
            if largest_digit == 0 or digit > largest_digit:
                largest_digit = digit
            if smallest_digit == 0 or digit < smallest_digit:
                smallest_digit = digit
        checksum = checksum + (largest_digit - smallest_digit)
    print("Day 2 part 1:" + str(checksum))

def day_two_part_two():
    data = read_file("input/day2part1")
    checksum = 0
    for row in data:
        find = False
        for digit_str in row:
            if find:
                break
            digit = int(digit_str)
            for digit_two_str in row:
                digit_two = int(digit_two_str)
                if digit == digit_two:
                    continue
                if digit % digit_two == 0:
                    if digit > digit_two:
                        checksum = checksum + (digit / digit_two)
                    else:
                        checksum = checksum + (digit_two / digit)
                    find = True
                    break
    print("Day 2 part 2:" + str(checksum))
