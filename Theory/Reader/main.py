file = open('export_imports.txt')

while True:
    line = file.readline()

    if not line:
        break

    item = line.split()

    if item[1] == 'E':
        print(item[0],":",item[2])

file.close()