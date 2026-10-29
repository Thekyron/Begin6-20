'''
#string2
N = int(input(''))
print(chr(N))

#string3
C = int(input(''))
print(chr(C-1))
print(chr(C+1))


#string4
n = int(input())
result = "".join(chr(65 + i) for i in range(n))
print(result)



#string5
n = int(input())
result = "".join(chr(122 - i) for i in range(n))
print(result)


#string7
s = input()
print(ord(s[0]), ord(s[-1]))


#string8
n = int(input())
c = input()
print(c * n)


#string9
n = int(input())
c1 = input()
c2 = input()

print((c1 + c2) * (n // 2))


#string12
s = input()
n = int(input())
stars = "*" * n
result = stars.join(s)
print(result)

string14
s = input()
count = sum(1 for char in s if 'A' <= char <= 'Z')
print(count)

string15
s = input()
count = 0
for char in s:
    if ('a' <= char <= 'z') or ('а' <= char <= 'я') or (char == 'ё'):
        count += 1
print(count)
'''