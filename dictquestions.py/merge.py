d1={"a": 1, "b": 2}
d2={"c": 3}

for key,val in d2.items():
    d1[key]=val

print(d1)

#d1.update(d2)