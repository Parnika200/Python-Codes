str="hello,how are u?"
r=""
for i in str:
    if i.isalnum():
        r+=i
print(r)

#if i not in str.punctuation