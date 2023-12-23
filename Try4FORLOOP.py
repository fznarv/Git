

with open('Try4FORLOOP.txt', 'r+') as file:
    context = file.read()
    file.seek(0)
    i = 1
    for name in file:
        print(f'{i}. {name}', end='')
        i += 1



