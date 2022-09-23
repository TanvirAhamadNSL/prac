# n, m = map(int, input().split())
# c = '.|.'

# a = int((n-1)/2)
# b = int((m-3)/2)
# #Top Con
# for i in range(a):
#     print((c*i).rjust(b, '-')+c+(c*i).ljust(b, '-'))


# print('WELCOME'.center(m,'-'))

# for i in range(a):
#     i = a - i -1
#     print((c*i).rjust(b, '-')+c+(c*i).ljust(b, '-'))



def my_deco(f):
    def wrapper():
        print("ha ha ha")
        f()
        print("ha ha ha")
    return wrapper


def fa():
    print("a")

def fb():
    print("b")

fa = my_deco(fa)

fa()
print("-------------------")
fb()