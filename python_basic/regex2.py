import re

for _ in range(int(input())):
    a, b= map(int, input().split())
    try:
        print(a/b)
    except Exception as e:
        print("Error Code:", e)