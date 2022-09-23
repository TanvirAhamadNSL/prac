import string


def print_formatted(number):
    for i in range(1,number+1):
        a = ""
        b = str(oct(i))
        c = str(hex(i))
        d = str(bin(i))
        a = a + i + ' ' + b + ' ' + c + ' ' + d
        print(a)
    return 0 

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)