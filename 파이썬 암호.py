code1 = ("EULJI UNIVERSITY")
code2 = ("IN SEONGNAM")


















print(type(code1))
print(type(code2))

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

