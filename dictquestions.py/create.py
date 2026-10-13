student={
    "name":"parnika",
    "marks":99,
    "age":20
}

student["city"]="pune"
student["marks"]=100

del student["city"]

student.pop("city",None)
print(student["marks"])
print(student)

if student["marks"]:
    print("yes")

for key,val in student.items():
    print(key,val)