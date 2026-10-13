file = open("Questions/filequestions/demo.txt", "r")

lines=file.readlines()
print(len(lines))
file.close()