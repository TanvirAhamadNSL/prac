"""
this a code
"""

if __name__ == '__main__':
    n = int(input())
    avgVal = 0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in range(3):
        avgVal += student_marks[query_name][i]
    avgVal = (avgVal/3)
    res = "{:.2f}".format(avgVal)
    print(res)
