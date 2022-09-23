data = [
    {
        "name":"tanvir",
        "age" : 36,
        "country" : "bangladesh"
    },
    {
        "name":"nuhash",
        "age" : 36,
        "country" : "india"
    }
]
data1 = ['india', 'bangladesh']

data1 = sorted(data1, reverse=False)
print(data1)
# # sort by age and name and then by country

# data = sorted(data, key=lambda x: x["age"], reverse=True)

# # output
# for item in data:
#     print(item["name"])
