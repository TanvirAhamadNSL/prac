if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    fianl = []
    sub1 = [i for i in range(0, (x+1))]
    sub2 = [j for j in range(0, (y+1))]
    sub3 = [k for k in range(0, (z+1))]
    final = [[l,m,o]for l in [i for i in range(0, (x+1))] for m in [j for j in range(0, (y+1))] for o in [k for k in range(0, (z+1))] if sum([l,m,o])!= n]
    print(final)
    