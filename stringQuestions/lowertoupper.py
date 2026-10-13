str="PytHoN"
r=""
for i in str:
    if i.isupper():
        r+=i.lower()
    elif i.islower():
        r+=i.upper()

print(r)

#print(str.swapcase())