f = open("data_1.txt", "w")
f.write("Hello World\n")

content = input()
f.write(f"{content}\n")

f.close()