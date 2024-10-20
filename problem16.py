size = 5
lastEvenNumber = size * 2
evenNumber = lastEvenNumber
for i in range(1, size + 1):
    evenNumber = lastEvenNumber
    for j in range(i):
        print(evenNumber, end=' ')
        evenNumber -= 2
    print()