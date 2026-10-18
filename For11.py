N = int(input("Введите N: "))

S = 0

for i in range(N, 2 * N + 1):
    S += i ** 2

print("Сумма квадратов:", S)