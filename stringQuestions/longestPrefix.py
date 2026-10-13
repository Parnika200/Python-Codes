words = ["flower", "flow", "flight"]
prefix=words[0]

for i in words:
    while not i.startswith(prefix):
        prefix=prefix[:-1]

print(prefix)