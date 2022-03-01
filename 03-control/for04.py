"""
Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8).
"""
N = int(input("Write N for factor:"))
while N > 8:
    N = int(input("N must be <= 8. Type another:.."))
fac = 1
if N == 0:
    print("0! = 1")
elif N == 1:
    print("1! = 1")
else:
    print(f'{N}! = ', end="")
    for i in range(1, N+1):
        fac = fac*i
        print(f'{i}', end="")
        if i == N:
            print(f' = {fac}')
        else:
            print(" *", end=" ")

