
a=float(input('введите цену за 1кг конфет '))

for i in range(1,11):
    w = i / 10
    total = a * w
    print(f"{total} цена за {w}кг конфет")