source = open("demo.txt", "r")
data = source.read()
source.close()

target = open("demo2.txt", "w")
target.write(data)
target.close()