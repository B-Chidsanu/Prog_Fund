r = float(input("Get value: "))
h = float(input("Get value: "))
area = 3.01 * r * r * h
print("Area= ", area)


#  ข้อ1
b = float(input("get value base: "))
h = float(input("get value height: "))
area = 0.5 * b * h
print("Area = ", area)


# ข้อ2
r = int(input("Get value radius: "))
h = int(input("Get value height: "))
area = 3.14 * r * r * h
print("Area = ", area)


# ข้อ3
h = int(input("Enter current Hour: "))
m = int(input("Enter current Min: "))
s = int(input("Enter current Sec: "))
print("Current time: ", f"{h:02d}:{m:02d}:{s:02d}")


# ข้อ4
homework = int(input("คะแนนเก็บ :"))
midterm = int(input("คะแนนกลางภาค :"))
final = int(input("คะแนนสอบปลายภาค :"))
total = (homework/100*10)+(midterm/100*40)+(final/100*50)
print("Total : ", total)


# ข้อ5
x1 = float(input("num1 : "))
x2 = float(input("num2 : "))
x3 = float(input("num3 : "))
x4 = float(input("num4 : "))
mean = int((x1+x2+x3+x4)/4)
print("Mean ", mean)


# ข้อ6
g1 = float(input("num1 : "))
g2 = float(input("num2 : "))
g3 = float(input("num3 : "))
g5 = float(input("num5 : "))
total = (g1+g2+g3+g4+g5)/5
print(format(total, '.3f'))


# ข้อ7
a, b, c = input().split()
c = int(c)
d = (a+b)*c
c = str(c)
print(a + b + c + d)


# ข้อ8
id = input("Student_id: ")
name = input("Your Name: ")
year_entry = (id[0]+id[7])
Last_4_Didit = (id[4]+id[5]+id[6]+id[7])
print("Student_id: ", id)
print("Name: ", name)
print("Year_Entry: ", year_entry)
print("Last_4_Didit: ", Last_4_Didit)
print("Department: Computer Engineering")


# ข้อ9
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
x1 = (-(b)+(b**2-(4*a*c))**0.5)/2*a
x2 = (-(b)-(b**2-(4*a*c))**0.5)/2*a
print("X", x1, ",", x2)


# ข้อ10
id = input("Your id: ")
id1 = int(id[0])*13
id2 = int(id[1])*12
id3 = int(id[2])*11
id4 = int(id[3])*10
id5 = int(id[4])*9
id6 = int(id[5])*8
id7 = int(id[6])*7
id8 = int(id[7])*6
id9 = int(id[8])*5
id10 = int(id[9])*4
id11 = int(id[10])*3
id12 = int(id[11])*2
a = id1+id2+id3+id4+id5+id6+id7+id8+id9+id10+id11+id12
b = a % 11
c = str(11-b)
print("Last digit number: ", c[len(c)-1])
