#lambda function

import re


def func(fun, val):
    return fun(val)

print(func(lambda X: X + 5, 5))

#map 
ls = [1,2,3,4,5,6]
result = list(map(lambda x: x+5, ls))
print(result)

#filter
res = list(filter(lambda x: x%2==0, ls))
print(res)

#generator
def generator