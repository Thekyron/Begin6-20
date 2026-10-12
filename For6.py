a=float(input('ведите цену за 1кг'))

for i in range(12, 21, 2):
    w=i/10
    total=a*w
    print(f"{total} цена за {w}кг конфет")