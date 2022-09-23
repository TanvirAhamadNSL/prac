from copy import deepcopy


def multi(a,b):
    return a * b

def div(a,b):
    return a / b

if __name__== '__main__':
    a = int(input())
    b = int(input())

    if b>a:
        temp = a
        a = deepcopy(b)
        b = deepcopy(temp)

    print(div(a,b))