
# ข้อ1
r = int(input("Enter interest rate: "))
m = [10000, 15000, 20000, 25000, 30000, 35000, 40000]
y = [1, 2, 3, 4]
total = []
for i in range(len(y)):
    for a in range(len(m)):
        sum = int(m[a])*((1+r/100)**int(y[i]))
        total.append('%.2f' % sum)

print(f"year      1        2        3        4")
for i in range(7):
    print(f"{m[i]}|{total[i]}|{total[i+7]}|{total[i+14]}|{total[i+21]}|")


# ข้อ2
time_in = int(input("Enter TimeIn: "))
time_minute_in = int(input("Enter Time Minute In: "))
time_out = int(input("Enter Time Out: "))
time_minute_out = int(input("Enter Time Minute Out: "))
In = (time_in*60)+time_minute_in
Out = (time_out*60)+time_minute_out
summin = Out-In
if In <= 15:
    print("Free")
elif summin > 15 and summin <= 180:
    cost = (summin // 60)+1
    if summin % 60 == 0:
        cost = (summin // 60)
    print("Total:", cost * 10, "Baht")
elif summin > 180 and summin <= 360:
    sum = summin - 180
    cost = (summin // 60)+1
    if summin % 60 == 0:
        cost = (summin // 60)
    print("Total:", (cost*20)+30, "Baht")
elif summin >= 360:
    print("Total:", 200, "Baht")


# ข้อ3
list = [2, 3, 5, 7, 11, 13, 17, 19]
sum = 1
for i in range(8):
    n = list[i]
    a = 1
    while True:
        if (n**a) > 20:
            sum *= n**(a-1)
            break
        a += 1
print("=", sum)


# ข้อ4
list = []
num = 600851475143
sum = 2
while True:
    if (num % sum) == 0:
        list.append(sum)
        num = num / sum
    if num == 1:
        break
    sum += 1
print(list)


# ข้อ5
def isprime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


list = []
count = 0
i = 2
while True:
    if isprime(i):
        list.append(i)
        count += 1
    if count >= 1001:
        list = list[-1:]
        break
    i += 1
print("Prime Number 1001 =", *list, sep=(" "))


# ข้อ6
a = int(input("Enter input: "))
sum_o_s = 0
s_o_sum = 0
for i in range(1, a+1):
    sum_o_s += i**2
    s_o_sum += i
    b = s_o_sum**2
    c = b - sum_o_s
    print(f'{b}-{sum_o_s} = {c}')


# ข้อ7
num = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
a = 0
str = ''
for i in range(len(num)-8):
    n = num[i:i+8]
    sum = 1
    for i in range(8):
        sum *= int(n[i])
    if sum >= a:
        a = sum
        str = n
print("เลขแปดตัวที่ติดกัน=", str, "ผลคูณที่มากที่สุด=", a)


# ข้อ8
Num_In = [int(g) for g in input("Enter 10 Number: ").split()]
list = []
list1 = []
for i in range(0, len(Num_In)):
    if Num_In[i] == 0:
        list.append(Num_In[i])
for i in range(0, len(Num_In)):
    if Num_In[i] != 0:
        list1.append(Num_In[i])
Logic = True
while Logic:
    Logic1 = False
    for i in range(0, len(list1)):
        if i + 1 > len(list1)-1:
            break
        elif list1[i] > list1[i+1]:
            list1[i], list1[i+1] = list1[i+1], list1[i]
            Logic1 = True
    Logic = Logic1
for i in list:
    list1.insert(1, 0)
print("คำตอบ: ", *list1, sep="")


# ข้อ9
num = 0
for i in range(100, 1000):
    for g in range(100, 1000):
        n = i*g
        nStr = str(n)
        if nStr == nStr[::-1]:
            if n >= num:
                num = n
print("Max Palindome Number =", num)
