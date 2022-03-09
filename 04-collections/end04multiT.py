n = 10
print("Multiplication Tables")
multiT = [[0]*n] * n
print(multiT)

for x in range(1, n+1):
    for y in range(1, n+1):
        multiT[x-1][y-1] = x * y

for row in multiT:
    for col in row:
        print(col, end="\t ")
    print()
