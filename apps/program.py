from apps.utils import int1,int2


def add(a,b) :
    val = int1(a,b)
    if a > b:
        return a+b+val
    else:
        return a+b

def sub(a,b):
    val = int2(a,b)
    return a-b

def mul(a,b):
    return a*b

