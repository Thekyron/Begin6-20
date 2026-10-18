N = int(input("Введите N: "))

P = 1

for i in range(1, N + 1):
    P *= 1 + i / 10

print("Произведение:", P)