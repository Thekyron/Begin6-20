a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a % 2 != 0 and b % 2 != 0:
    print('ошибка')
elif a % 2 != 0 or b % 2 != 0:
    print('норм')
else:
    print('плохо')