str="level 12 #"
v=0
d=0
s=0
c=0
con=0
for i in str:
    if i in 'aeiou':
        v+=1
    elif i.isdigit():
        d+=1
    elif i.isspace():
        s+=1
    elif not i.isalnum():
        c+=1
    else:
        con+=1

print(v,d,s,c,con)

