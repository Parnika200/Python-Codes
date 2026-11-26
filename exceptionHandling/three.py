class Custom(Exception):
    pass


try:
    set={101,202,303}
    n=int(input("enter id"))
    if n in set:
        raise Custom("id already exists")
    else:
        set.add(n)
except Custom as e:
    print(e)


