"""
place where python stores names,functions

1.LOCAL- inside current function
2.ENCLOSING- outer function
3.GLOBAL- module/file level
4.BUILT IN - print()
"""

x=10
def fun():
    global x #used to modify global variable
    x=20
    print(x)

fun() 
print(x)


def outer():
    x=10

    def inner():
        nonlocal x #change enclosing variable
        x=9
        print(x)

    inner()
    print(x)
outer()


print(globals())
print(locals())