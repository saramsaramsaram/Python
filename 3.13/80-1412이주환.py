f = open("data_2.txt", "r")
lines = f.readlines()
print(lines)

for i in lines:
    print(i)
f.close()