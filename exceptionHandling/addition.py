try:
    n=int(input("enter num"))
    n1=int(input("enter num"))
    sum=n1+n
except ValueError:
    print("onli int")
except TypeError:
    print("cannot be devided")
else:
    print(sum)