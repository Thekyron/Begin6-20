A=int(input('введите первое целое число(A<B) '))
B=int(input('введите второе целое число '))
for i in range(A, B+1):
    print(i, end="")
print()
N=B-A+1
print(f'{N} чисел')