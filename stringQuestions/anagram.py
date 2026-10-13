s1 = input("Enter first string: ").lower()
s2 = input("Enter second string: ").lower()
d={}
for i in s1:
    d[i]=d.get(i,0)+1

for i in s2:
    if i not in d:
        print("not anagram")
        break
    d[i]-=1
    if d[i]<0:
        print("not anagram")
        break
    else:
        print("anagram")

    
