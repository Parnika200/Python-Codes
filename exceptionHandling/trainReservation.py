class Custom(Exception):
    pass

train={
    "A":20,
    "B":30,
    "C":40
}

try:
    n=input("enter train name")
    seats=int(input("enter seats"))
    if n not in train:
        raise Custom("train does not exist")
    if seats>train[n]:
        raise Custom("seats not available")
    else:
        print("booking done")
        train[n]-=seats
except Custom as e:
    print(e)