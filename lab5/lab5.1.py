# ข้อ1
num = int(input("Enter N: "))
text = ""
text1 = ""
half = ""
list = []
list1 = []
if num < 0 or num > 9:
    print("error")
else:
    for i in range(0, num+1):
        n = str(i)*((num-i)+(num-i)+1)

        for j in range(0, i):
            text += str(j)
            text1 = text[::-1]
        half = text + n + text1
        list.append(half)
        text = ""

    for r in range(len(list)):
        list1.append(list[-(r+1)])

    for p in range(len(list)):
        print(f"{list[p]}")

    for u in range(1, len(list1)):
        print(f"{list1[u]}")
