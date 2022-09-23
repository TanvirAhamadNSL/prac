from audioop import reverse


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    arr.sort(reverse=True)
    out = arr[0]
    for i in arr:
        if i<out:
            print(i)
            break
