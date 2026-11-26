data = ["100", "200", None, "ABC", "400"]


try:
    i=int(input("enter index"))
    n=int(data[i])
except ValueError:
    print("index must be in int")
except IndexError:
    print("index out of range")
except TypeError:
    print("cannot convert")
else:
    print(n)
    
