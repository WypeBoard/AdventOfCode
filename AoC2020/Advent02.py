from helpers import readFile


def sanitizeInput(data):
    query = data.split(" ")
    return int(query[0]), int(query[1]), query[2], query[3]


def partone(data):
    currectPasswords = 0
    for passwordLine in data:
        initial, last, delimiter, password = sanitizeInput(passwordLine)
        passwordRequirement = password.count(delimiter)
        if initial <= passwordRequirement <= last:
            currectPasswords = currectPasswords + 1
    return currectPasswords


def check_char(char, requirement):
    return char is requirement


def parttwo(data):
    currectPasswords = 0
    for passwordLine in data:
        initial, last, delimiter, password = sanitizeInput(passwordLine)
        first_char = password[initial - 1]
        last_char = password[last - 1]
        if first_char is not last_char and (check_char(first_char, delimiter) or check_char(last_char, delimiter)):
            currectPasswords = currectPasswords + 1
    return currectPasswords


if __name__ == '__main__':
    values = readFile.readcsv('inputs/day02.csv')
    print(partone(values))
    print(parttwo(values))
