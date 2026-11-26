employees = {
    101: {"name": "Amit", "salary": 30000},
    102: {"name": "Priya", "salary": 40000},
    103: {"name": "Rahul", "salary": 35000}
}

try:
    n=int(input("enter id"))
    name=input("name")
    emp=employees[n]
    i=emp[name]
    print(emp)
    print(i)
except ValueError:
    print("wrong values")
except KeyError:
    print("key does not exist")
else:
    print("no error")