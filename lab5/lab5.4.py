# ข้อ4
data = [
    "*****",
    "*MM**",
    "*KIK*",
    "*IT**",
    "**L**"]


def genlist(text, pos):
    u = []
    # ขวาล่าง
    if data[int(pos.split(",")[0])+1][int(pos.split(",")[1])+1] == text:
        u.append(f"{int(pos.split(',')[0])+1},{int(pos.split(',')[1])+1}")

    # กลางล่าง
    if data[int(pos.split(",")[0])+1][int(pos.split(",")[1])+0] == text:
        u.append(f"{int(pos.split(',')[0])+1},{int(pos.split(',')[1])+0}")

    # ซ้ายล่าง
    if data[int(pos.split(",")[0])+1][int(pos.split(",")[1])-1] == text:
        u.append(f"{int(pos.split(',')[0])+1},{int(pos.split(',')[1])-1}")

    # กลางขวา
    if data[int(pos.split(",")[0])+0][int(pos.split(",")[1])+1] == text:
        u.append(f"{int(pos.split(',')[0])+0},{int(pos.split(',')[1])+1}")

    # กลางซ้าย
    if data[int(pos.split(",")[0])+0][int(pos.split(",")[1])-1] == text:
        u.append(f"{int(pos.split(',')[0])+0},{int(pos.split(',')[1])-1}")

    # ขวาบน
    if data[int(pos.split(",")[0])-1][int(pos.split(",")[1])+1] == text:
        u.append(f"{int(pos.split(',')[0])-1},{int(pos.split(',')[1])+1}")

    # กลางบน
    if data[int(pos.split(",")[0])-1][int(pos.split(",")[1])+0] == text:
        u.append(f"{int(pos.split(',')[0])-1},{int(pos.split(',')[1])+0}")

    # ซ้ายบน
    if data[int(pos.split(",")[0])-1][int(pos.split(",")[1])-1] == text:
        u.append(f"{int(pos.split(',')[0])-1},{int(pos.split(',')[1])-1}")
    return u


list_K = []
list_M = []
list_I = []
list_T = []
list_L = []
answer2 = []
for i in range(0, len(data)):
    if "K" in data[i]:
        for j in range(0, len(data)):
            if data[i][j] == "K":
                list_K.append(f"{i},{j}")

for K in list_K:
    for M in genlist("M", K):
        list_M.append(M)
        for I in genlist("I", M):
            list_I.append(I)
            for T in genlist("T", I):
                list_T.append(T)
                for L in genlist("L", T):
                    list_L.append(L)
                    answer2.append(
                        f"K{int(K.split(',')[0])+1},{int(K.split(',')[1])+1} M{int(M.split(',')[0])+1},{int(M.split(',')[1])+1} I{int(I.split(',')[0])+1},{int(I.split(',')[1])+1} T{int(T.split(',')[0])+1},{int(T.split(',')[1])+1} L{int(L.split(',')[0])+1},{int(L.split(',')[1])+1}")

print(*answer2, sep=("\n"))
print("KMITL Count =", len(answer2))
