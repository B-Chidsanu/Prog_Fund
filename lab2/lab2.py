
# ข้อ1
num = int(input("Enter x: "))
if num % 5 == 0:
    print(num, "is divisible by 5")  # หารด้วย 5 ลงตัว
else:
    print(num, "is not divisible by 5")  # หารด้วย 5 ไม่ลงตัว


# ข้อ2
x = int(input("Enter x: "))
if 80 <= x <= 100:
    print('G')  # Good
elif 50 <= x < 80:
    print('P')  # PAss
elif 0 <= x < 50:
    print('F')  # Fail
else:
    print('Error')


# ข้อ3
m_score = int(input("Enter midterm: "))
f_score = int(input("Enter final: "))
h_score = int(input("Enter homework: "))
x = m_score*0.4 + f_score*0.5 + h_score
if x < 0 or x > 100:
    print('Error')
elif 90 <= x <= 100:
    print('A')
elif 85 <= x <= 90:
    print('B+')
elif 80 <= x < 85:
    print('B')
elif 70 <= x < 80:
    print('C+')
elif 60 <= x < 70:
    print('C')
elif 55 <= x < 60:
    print('D+')
elif 50 <= x < 55:
    print('D')
else:
    x < 50
    print('F')


# ข้อ4
x = int(input("Enter x: "))
y = int(input("Enter y: "))
if x > y:
    print("Maximum is:", x)
else:
    y > x
    print("Maximum is:", y)


# ข้อ5
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
if a > b and a > c:
    if b > c:
        print("ค่ากลาง=", b)
    else:
        print("ค่ากลาง=", c)
if b > a and b > c:
    if a > c:
        print("ค่ากลาง=", a)
    else:
        print("ค่ากลาง=", c)
if c > a and c > b:
    if a > b:
        print("ค่ากลาง=", a)
    else:
        print("ค่ากลาง=", b)


# ข้อ6
age = int(input("Enter your age: "))
if age < 0:
    print("error")
if 0 <= age <= 10:
    print("Children")
if 11 <= age <= 20:
    print("Teenage")
if 21 <= age <= 35:
    print("Adult")
if 36 <= age <= 55:
    print("Middle age")
if age >= 56:
    print("Old age")


# ข้อ7
x = int(input("Select 1(Rectangle) or Select 2(Triangle): "))
if x == 1:
    r = input("width,leght: ")
    r1, r2 = r.split(",")
    r3 = int(r1) * int(r2)
    print("Rectangle Area = ", r3)
elif x == 2:
    t = input("base,height: ")
    t1, t2 = t.split(",")
    t3 = 0.5 * int(t1) * int(t2)
    print("Triangle Area = ", t3)


# ข้อ8 แก้
x = int(input("Enter month: "))
a = x-1
monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
             'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
if 0 < x <= 12:
    print('Month: ', monthlist[a])
else:
    print('error')


# ข้อ9
n = int(input("Enter an integer N: "))
if n >= 0:
    n = n % 10
else:
    n = -n % 10
NList = ['Zero', 'One', 'Two', 'Three', 'Four',
         'Five', 'Six', 'Seven', 'Eight', 'Nine']
print(NList[n])


# ข้อ10
years = int(input("Enter year: "))
if years % 400 == 0:
    print("Leap year")
elif years % 100 == 0:
    print("Don't Leap year")
elif years % 4 == 0:
    print("Leap year")


# ข้อ11
a1, a2, a3, a4, a5 = [int(e) for e in input("Enter: ").split()]
s = 0
if a1 < a2 < a3 < a4 < a5:
    print("True")
else:
    print("False")


# ข้อ12
a1, a2, a3, a4 = [int(e) for e in input("Enter 4 number: ").split()]
list = [a1, a2, a3, a4]
max = max(list)
min = min(list)
t = sum(list)-(max+min)
print(t)


# ข้อ13
a = False
b = False
print("\n Pizza small size 99 THB\n Pizza Medium size 199 THB\n Pizza Large size 299 THB")
size = input("Please select size: ")
if size == "1":
    Cheese = input("Pizza small size add cheese 20 THB Y/N: ").upper()
    Extra = input("Do you want Extra too? Add money 20 THB Y/N: ").upper()
    total = 99
    if Cheese in "Y":
        total = 99 + 20
    elif Cheese in "N":
        total = total
    elif Cheese not in "YN":
        a = True
    if Extra in "Y":
        total += 20
    elif Extra in "N":
        total = total
    elif Extra not in "YN":
        b = True

elif size == "2":
    Cheese = input("Pizza Medium size add cheese 30 THB Y/N: ").upper()
    Extra = input("Do you want Extra too? Add money 20 THB Y/N: ").upper()
    total = 199
    if Cheese in "Y":
        total = 199 + 30
    elif Cheese in "N":
        total = total
    elif Cheese not in "YN":
        a = True
    if Extra in "Y":
        total += 20
    elif Extra in "N":
        total = total
    elif Cheese not in "YN" or Extra not in "YN":
        b = True

elif size == "3":
    Cheese = input("Pizza Large size add cheese 40 THB Y/N: ").upper()
    Extra = input("Do you want Extra too? Add money 20 THB Y/N: ").upper()
    total = 299
    if Cheese in "Y":
        total = 299 + 40
    elif Cheese in "N":
        total = total
    elif Cheese not in "YN":
        a = True
    if Extra in "Y":
        total += 20
    elif Extra in "N":
        total = total
    elif Cheese not in "YN" or Extra not in "YN":
        b = True

else:
    total = "error"
if a or b:
    total = "error"
print(f"total = {total}")
