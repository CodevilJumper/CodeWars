size = 3

for line in range(1, size + 1):
    for space in range(1, size - line + 1):
        print(' ', end = '')
    for asterix in range(1, line + 1):
        print('*', end = '')
    print()
