if __name__ == '__main__':
    main_list = []
    n = int(input())
    for _ in range(n):
        sub_list = []
        sub_list.append(float(input()))
        sub_list.append(input())
        main_list.append(sub_list)
    main_list.sort()
    min = main_list[0][0]
    for i in range(n):
        if min == main_list[i][0]:
            continue
        elif min < main_list[i][0]:
            goal = main_list[i][0]
            break
    for i in range(n):
        if goal == main_list[i][0]:
            print(main_list[i][1]) 