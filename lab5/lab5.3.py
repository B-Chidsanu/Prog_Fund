# ข้อ3
import random
data = {}
foundWinner = False


def table():
    for i in range(1, 7):
        print(f"{i}| {data.get(f'{i}1',' ')} | {data.get(f'{i}2',' ')} | {data.get(f'{i}3',' ')} | {data.get(f'{i}4',' ')} | {data.get(f'{i}5',' ')} | {data.get(f'{i}6',' ')} | ")
    print(f"   {1}   {2}   {3}   {4}   {5}   {6}")


def drop(y, type):
    for x in range(6, 0, -1):
        if data.get(str(x)+str(y), False):
            continue
        else:
            if (type == 1):
                data[str(x)+str(y)] = "x"
            elif (type == 2):
                data[str(x)+str(y)] = "w"
            check(x, y)
            break


def check(x, y):
    global foundWinner
    # แนวตั้ง
    # บนลงล่าง
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x)+str(y-1), False)
    check3 = data.get(str(x)+str(y-2), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True
    # ล่างขึ้นบน
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x)+str(y+1), False)
    check3 = data.get(str(x)+str(y+2), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True
    # บน-กลาง-ล่าง
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x)+str(y+1), False)
    check3 = data.get(str(x)+str(y-1), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True

    # อันนี้แนวนอนนะ
    # ขวาไปซ้ายเลย
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x-1)+str(y), False)
    check3 = data.get(str(x-2)+str(y), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True
    # ซ้ายไปขวาเลย
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x+1)+str(y), False)
    check3 = data.get(str(x+2)+str(y), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True
    # กลางออกข้าง
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x+1)+str(y), False)
    check3 = data.get(str(x-1)+str(y), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True

    # แนวเฉียง
    # เฉียงบนลง
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x+1)+str(y-1), False)
    check3 = data.get(str(x+2)+str(y-2), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True
    # เฉียงล่างขึ้นบน
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x-1)+str(y+1), False)
    check3 = data.get(str(x-2)+str(y+2), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True
    # เฉียงบน-กลาง-ล่าง
    check1 = data.get(str(x)+str(y), False)
    check2 = data.get(str(x-1)+str(y+1), False)
    check3 = data.get(str(x+1)+str(y-1), False)
    if (check1 == "x" and check2 == "x" and check3 == "x"):
        print("User Win")
        foundWinner = True
    elif (check1 == "w" and check2 == "w" and check3 == "w"):
        print("Computer Win")
        foundWinner = True


while True:
    table()
    while True:
        n = int(input("Enter number (1-6): "))
        if n > 6 or n < 1:
            print("error")
        else:
            drop(n, 1)
            table()
            if (foundWinner):
                t = input("เล่นต่อหรือไม่? Y/N: ")
                if t == "Y":
                    data.clear()
                    foundWinner = False
                elif t == "N":
                    break
                else:
                    print("error")
                    break
                break
            computer = random.randint(1, 6)
            drop(computer, 2)
            table()
            if (foundWinner):
                t = input("เล่นต่อหรือไม่? Y/N: ")
                if t == "Y":
                    data.clear()
                    foundWinner = False
                elif t == "N":
                    break
                else:
                    print("error")
                    break
                break
    if t != "Y":
        break
