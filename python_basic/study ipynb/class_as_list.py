class abc():
    def __init__(self):
        self.car = {}
    def __setitem__(self,index, brand):
        self.car[index] = brand
    def __getitem__(self, item):
        return self.car[item]
        

a = abc()
a[0] = 'BMW'
a[1] = 'AUDI'

print(a[1])