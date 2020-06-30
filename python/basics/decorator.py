# decorator
# Need to return a function to make sure that the original function
# is still functional
# With parameters, the decorator need to take the parameters too.

#  decorator with no parameters
def decNoPara(f):
    def inner():
        print("start inner")
        f()
        print("after inner")

    return inner


def decWithPara(f):
    def inner(*para, **kwpara):
        print("with para start")
        res = f(*para, **kwpara)
        print("with para after")
        return res

    return inner


@decNoPara
@decWithPara
def sampleFunc1():
    print("function1")


@decWithPara
def sampleFunc2():
    print("function2")


sampleFunc1()
sampleFunc2()
