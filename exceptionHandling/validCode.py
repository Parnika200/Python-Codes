
class Custom(Exception):
    pass

code=123
i=0
while i<3:
    try:
        n=int(input("enter valid code"))
        if n!=code:
            i+=1
            raise Custom("invalid code")
        else:
            print("correct code")
            break
     
    except Custom as e:
        print(e)