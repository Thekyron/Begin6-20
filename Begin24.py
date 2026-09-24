A = float(input("введи первое число"))
B = float(input("введи второе число"))
C = float(input("введи третье число"))
temp = A
A = C
C = B
B = temp
print(A,B,C)