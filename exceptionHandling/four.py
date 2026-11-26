try:
    s=input("enter string")
    n=int(s)
except ValueError:
    print("cannot be converted")
else:
    print(n)