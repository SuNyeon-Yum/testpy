code1 = ("EULJI UNIVERSITY")
code2 = ("IN SEONGNAM")

print('')
print('이 암호는 일정한 규칙을 가지고 있는 암호입니다.')
print('간단한 수학적 접근이 필요하며, 암호를 풀어보세요.') 

str=''

print()

for i in code1:
    if ord(i) >= ord ('A') and ord(i) <=ord('Z'):
        print(chr(ord(i)-2),end='I')
        str=str+chr(ord(i)+1)


print()
print()

for i in code2:
    if ord(i) >= ord ('A') and ord(i) <=ord('Z'):
        print(chr(ord(i)-2),end='W')
        str=str+chr(ord(i)+1)

print()
