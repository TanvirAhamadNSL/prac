def fib(number):
    a, b = 0,1
    if number> 2:
        yield a
        yield b
        for i in range(0, num-1):
            temp = a+b
            a = b
            b = temp
            yield temp
    elif num == 1:
        yield a
    else:
        yield b
        yield a

if __name__ == '__main__':
    num = int(input())
    ch = True
    for i in fib(num):
        if i == 1 and ch:
            ch = False
            continue
        print(i)
