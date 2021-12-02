input = input("Input: ")
panjang = len(input)
print("Output :")
for i in range(0, panjang, 1):
    for j in range(0, i + 1):
        print(input[j], end='')
    print()
for i in range(panjang-1, 0, -1):
    for j in range(0, i):
        print(input[j], end='')
    print()