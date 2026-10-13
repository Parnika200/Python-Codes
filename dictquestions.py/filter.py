d={"A": 40, "B": 80, "C": 60}
res={}
for key,val in d.items():
    if val>50:
        res[key]=val

print(res)