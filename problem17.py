size = 7
row_len = 1
for i in range(size):
    for j in range(row_len):
        print(i * j, end=' ')
    row_len += 1
    print()