'''
err2
try:
    a = int(input())
    b = int(input())
    print(f"{a / b:.1f}")
except ZeroDivisionError:
    print("Делить на ноль нельзя")



err5
s = input()
i = int(input())

try:
    print(s[i])
except IndexError:
    print("Нет такого символа")



err6
s = input()

try:
    i = int(input())
    print(s[i])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")




err7
while True:
    try:
        n = int(input())
        break
    except ValueError:
        print("Это не число. Попробуй ещё:")

print(n)



err11
try:
    a = float(input())
    b = float(input())
    result = a / b
except (ValueError, ZeroDivisionError):
    print("Посчитать не удалось")
else:
    print(f"{result:.2f}")




err12
try:
    n = int(input())
except ValueError as e:
    print(e)
    print(type(e))
else:
    print(n)'''