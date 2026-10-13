file=open("filequestions/demo.txt", "r")

for l in file:
    if "python" in l:
        print(l)

file.close()