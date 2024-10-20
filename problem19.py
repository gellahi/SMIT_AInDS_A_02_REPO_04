size = 6
row_len = 1
for i in range(1, size):
    num = 1
    for j in range(1, size):
        if j < (size - row_len):
            print(' ', end=' ')
        else:
            print(num, end=' ')
            num += 1
    row_len += 1
    print()
