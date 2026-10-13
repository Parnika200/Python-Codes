str="python is easy"
words=str.split()
l=""
for word in words:
    if len(word)>len(l):
        l=word
print(l)

