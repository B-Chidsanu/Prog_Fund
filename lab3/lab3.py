
# ข้อ1
n = int(input("Enter your number: "))
sum = 0
for i in range(5, n+1, 5):
    sum = sum + i
print(sum)


# ข้อ2
n = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        n.append(i)
print(*n, sep=(","))


# ข้อ3
n = int(input("Enter your number: "))
sum = 0
for i in range(1, n+1):
    if i % 2 != 0 and i % 3 != 0 or i % 2 == 0 and i % 3 == 0:
        sum = sum + i
        print(i)
print(sum)


# ข้อ4 #แก้แล้ว
char = str(input('Enter str: '))
list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = 0
b = 0
for i in char:
    if i in list:
        a = a + 1
    elif i in list1:
        b = b + 1
if a == 0:
    print('Lower: ', b)
elif b == 0:
    print('Upper: ', a)
else:
    print(f'Upper:{a}, Lower: {b}')


# ข้อ5 #แก้ดัก0แล้ว
n = []
for i in range(1000, 3001):
    if i % 2000 < 1000 and i % 200 < 100 and i % 20 < 10 and i % 2 == 0:
        n.append(i)
print(*n, sep=(","))


# ข้อ7
a, b = input("Enter number: ").split()
a = int(a)
b = int(b)
sum = 0
if a <= 0 or b <= 0:
    print("Error")
else:
    for i in range(1, 10000):
        if a % i == 0 and b % i == 0:
            sum = i
    print(sum)


# ข้อ9
num = int(input("Enter number: "))
a = ""
b = ""
c = 0
for i in range(0, 4):
    a += str(num)
    b += "+" + a
    c += int(a)
print("Output: ", c, '(', "=", b[1:], ')')


# ข้อ10
n = input("Enter number: ")
num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
a = 0
for i in range(len(n)):
    if i > 0 and num[n[i]] > num[n[i-1]]:
        a += num[n[i]] - 2 * num[n[i-1]]
    else:
        a += num[n[i]]
print(n, '=', a)


# ข้อ11
n = int(input("Input: "))
a = 0
b = 1
c = "0,1"
if n < 0:
    print('|R: ')
else:
    for i in range(0, n):
        d = a+b
        a = b
        b = d
        if b < n:
            c += ','+str(b)
        else:
            break
print(f'{c}')
