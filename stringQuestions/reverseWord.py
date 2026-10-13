s = input("Enter a sentence: ")
words=s.split()
r=""
for i in words:
    r+=i[::-1]
print(r)