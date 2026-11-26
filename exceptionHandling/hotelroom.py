class Custom(Exception):
    pass

hotel={
    101:"blue hotel",
    202:"pink hotel",
    303:"rose hotel"
}

try:
    n=int(input("enter room number"))
    m=int(input("ente number of nights"))

    if m<=0 or m>15:
        raise Custom("num of nights should be between 1 to 15")

    print("room available",hotel[n])
except ValueError:
    print("wrong value")
except Custom as e:
    print(e)
except KeyError:
    print("room not available")
else:
    del hotel[n] # delete room if booked
    print("booking confirmed")