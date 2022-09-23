file = open('text.txt','r')
#text file contain 10 20 0
data = file.read()
ls = data.split("\n")
file.close()

try:
    print(int(ls[0])/int(ls[2]))
except ZeroDivisionError:
    print('Zero is not supported as denominator')
finally:
    print('this module run must after try and except')
    print('for raising any exception from user use raise command')
    raise TypeError


