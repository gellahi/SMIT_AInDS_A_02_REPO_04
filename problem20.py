size = 7
for i in range(size):
    for k in range(size - i - 1):
        print(' ', end='')
    for j in range(i + 1):
        print('*', end=' ')
    print()
