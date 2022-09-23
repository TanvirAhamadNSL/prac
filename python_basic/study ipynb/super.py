class parent:
    def __init__(self, name):
        self.name = name
    def __call__(self,  name1):
        self.name = name1
        return self.name
class child(parent):
    def __init__(self, height, width, name):
        super().__init__(name)
        self.height = height
        self.width = width

# a = child(10, 5, 'tanvir')
# print(a.name)

Parent = parent("nuhash")
y = Parent("yousuf")
print(y)