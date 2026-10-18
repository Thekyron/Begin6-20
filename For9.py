A = int(input("Введите A: "))
B = int(input("Введите B: "))

S = 0

for i in range(A, B + 1):
    S += i ** 2

print("Сумма квадратов:", S)