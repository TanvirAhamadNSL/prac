def count_substring(string, sub_string):
    a = 0
    for i in range(0, len(string)):
        if macher(string[i:(len(sub_string)+i)], sub_string):
            a += 1
    return a
def macher(split, sub_string):
    return split == sub_string

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print (count)