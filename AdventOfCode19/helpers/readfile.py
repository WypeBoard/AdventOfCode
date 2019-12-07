def readcsv(file_path):
    with open(file_path, 'r', newline='') as file:
        return [x.strip() for x in list(file.readlines())]

def readcsvmultiline(file_path):
    with open(file_path, 'r', newline='') as file:
        return [x.strip() for x in file.readlines()]