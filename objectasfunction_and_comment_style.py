def sum(a,b):
    """
    calculate the sum of two integer number

    return the sum
    """
    return a + b
def mul(a,b):
    #multiply two integer number. it is a single line comment.
    return a * b
def summul(a,b):
    return b(a,a) + b(a,a)

sum_as_var = sum
mul_as_var = mul

print(summul(2, mul))
print(sum_as_var(10,2))
print(mul_as_var(10,2))
print(sum.__doc__)



