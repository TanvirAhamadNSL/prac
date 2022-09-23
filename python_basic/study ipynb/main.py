from copy import deepcopy
from temp1 import mul
import fuction.sub1.func as fn
import sys
sys.path.insert(1, '/home/nsl50/Tanvir/python_basic/json_extraction')
import func1 as fn2
# import func1 as fn2
#from ..json_extraction import func1 as fn2

def sum(a,b):
    return a + b

def sub(a,b):
    return a - b

if __name__ =='__main__':
    a = int(input())
    b = int(input())
    data = [
        {
            "name":"b",
            "age" : 36,
            "country" : "bangladesh"
        },
        {
            "name":"b",
            "age" : 36,
            "country" : "india"
        },
        {
            "name":"c",
            "age" : 26,
            "country" : "pakistan"
        }
    ]

    if a < b:
        temp = a
        a = deepcopy(b)
        b = deepcopy(temp)

    print(sum(a,b))
    print(sub(a,b))

    print(mul(a,b))
    print(fn.multi(a,b))
    print(int(fn2.div(a,b)))