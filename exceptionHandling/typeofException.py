try:
    a=[10,20,30]
    print(a[4])
except Exception as e:
    print(type(e))
    print(str(e))


try:
    sum="anna"/3
    print(sum)
except Exception as e:
    print(type(e))
    print(str(e))