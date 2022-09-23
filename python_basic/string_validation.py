if __name__ == '__main__':
    s = input()
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    a5 = [] 
    for i in range(0,len(s)):
        a1.append(s[i].isalnum())
        a2.append(s[i].isalpha())
        a3.append(s[i].isdigit())
        a4.append(s[i].islower())
        a5.append(s[i].isupper())
    print(any(a1))
    print(any(a2))
    print(any(a3))
    print(any(a4))
    print(any(a5))
