size = 10
row_len = 1
for i in range(1, size + 1, +2):
    for j in range(row_len):
        print(i, end=' ')
    row_len += 1
    print()