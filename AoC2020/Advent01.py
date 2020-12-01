def partone(data):
    for i in data:
        for j in data:
            if i == j:
                pass
            if i + j == 2020:
                print(i, j)
                return i * j


def parttwo(data):
    for i in data:
        for j in data:
            for k in data:
                if i == j or j == k or i == k:
                    pass
                if i + j + k == 2020:
                    print(i, j, k)
                    return i * j * k


def readcsv(file_path):
    with open(file_path, 'r', newline='') as file:
        return [x.strip() for x in list(file.readlines())]


if __name__ == '__main__':
    values = readcsv('inputs/day01.csv')
    data = []
    for value in values:
        data.append(int(value))
    print(partone(data))
    print(parttwo(data))
