d1={"a": 1, "b": 2}
d2={"b": 3, "c": 4}
res=[]
for key in d1:
    if key in d2.keys():
        res.append(key)

print(res)