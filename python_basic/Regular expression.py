def check(a):
    assert open(a):
        print("file doesn't exist!")
    return 1

a = "text.txt"
print(check(a))
file_to_work = open("text.txt", "w")
file = file_to_work.write("I am writting!!\nLine 1\nLine 2")
file_to_work.close()

file_to_work = open("text.txt", "r")
file = file_to_work.read(1)
file1 = file_to_work.read(3)
file2 = file_to_work.readline()
file3 = file_to_work.readlines()


print(file)
print(file1)
print(file2)
print(file3)