A = float(input("Введите A: "))
N = int(input("Введите N: "))

P = 1

for i in range(N):
    P *= A

print("Результат:", P)