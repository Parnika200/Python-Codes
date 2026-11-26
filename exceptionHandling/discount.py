class Custom(Exception):
    pass

try:
    c=input("enter coupon code")
    p=int(input("enter purchase amt"))
    if c!="Save10" and c!="Save20":
        raise Custom("invalid coupon")
    if p<500:
        raise Custom("purchase should be >500")
except Custom as e:
    print(e)
else:
    print("discount applied")
    if c=="Save10":
        d=p*0.10
        p=p-d
        print(p,"afted discount")
    if c=="Save20":
            d=p*0.20
            p=p-d
            print(p,"afted discount")