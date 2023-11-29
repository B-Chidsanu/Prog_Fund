data = ["*****","*MM**","*KIK*","*IT**","**L**"]
print(data[2][1])
for i in range(0,len(data)):
    if "K" in data[i]:
        for j in range(0,len(data)):
            if data[i][j] == "K":
                list_K.append(f"{i},{j}")
                print(list_K)