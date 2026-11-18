"""
map = used to iterate over sequence
"""
from functools import reduce

#multiply each element by 2
l=[1,2,3,5,6]
res=list(map(lambda x:x*2,l))
print(res)

square=list(map(lambda x:x**2,l))
print(square)

# multiple lists
a=[1,2,3]
b=[2,3,4]
sum=set(map(lambda x,y:x+y,a,b))
print(sum)


# find len of names
names = ["Anna", "Jonathan", "Maya"]
l=list(map(lambda x:len(x),names))
print(l)


"""filter"""

list2=[1,2,3,4,5]

# find only odd elements
odd=list(filter(lambda x:x%2!=0,list2))
print(odd)


""" reduce  = combines all elements into one final result"""

sum2=reduce(lambda x,y:x+y,list2)
print(sum2)

# find max numbers
max=reduce(lambda x,y: x if x>y else y,list2)
print(max)

#cincatinate strings
words = ["Python", "is", "easy"]
c=reduce(lambda x,y:x +" "+y,words)
print(c)