A = int(input("Введите A: "))
B = int(input("Введите B: "))

P = 1

for i in range(A, B + 1):
    P *= i

print("Произведение:", P)