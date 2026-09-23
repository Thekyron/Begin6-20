x1 = float(input("введите первое число "))
y1 = float(input("введите второе число "))
x2 = float(input("введите третье число "))
y2 = float(input("введите четвертое число "))

a = abs(x2 - x1)
b = abs(y2 - y1)

P = 2 * (a + b)
S = a * b

print(P,S)