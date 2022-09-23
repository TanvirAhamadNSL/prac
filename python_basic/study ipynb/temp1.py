# def sorting(data):
#     data = sorted(data, key=lambda x:(x["age"],x["name"],x["country"]), reverse=True)
#     print(sorting(data))

# def mul(a,b):
#     return a*b

# def welcome():
#     print("welcome")
if __name__ == '__main__':
    data = [
        {
            "name":"b",
            "age" : 36,
            "country" : "bangladesh"
        },
        {
            "name":"b",
            "age" : 36,
            "country" : "india"
        },
        {
            "name":"c",
            "age" : 26,
            "country" : "pakistan"
        }
    ]
    data = sorted(data, key=lambda x:(x["age"],x["name"],x["country"]), reverse=True)
    print(data)
    