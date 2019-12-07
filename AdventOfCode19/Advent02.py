import math

from helpers import readfile

def executeprogram(data, pos_1, pos_2):
    memory = data.copy()
    memory[1] = pos_1
    memory[2] = pos_2
    position = 0
    while True:
        if memory[position] == 1:
            memory[memory[position + 3]] = memory[memory[position + 1]] + memory[memory[position + 2]]
            position += 4
        elif memory[position] == 2:
            memory[memory[position + 3]] = memory[memory[position + 1]] * memory[memory[position + 2]]
            position += 4
        elif memory[position] == 99:
            break
    return memory



def partone(data):
    print(executeprogram(data, 12, 2)[0])


def parttwo(data):
    for x in range(100):
        for y in range(100):
            res = executeprogram(data, x, y)
            if res[0] == 19690720:
                print('x = {0}, y = {1}'.format(x,y))
                print(100*x+y)



if __name__ == '__main__':
    values = readfile.readcsv('inputs/day02.csv')
    data = []
    for value in values:
        data.append(int(value))
    partone(data)
    parttwo(data)
