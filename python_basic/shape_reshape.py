import numpy


#shape and Reshape
#op = numpy.asarray(list(map(int,input().split())))
#print(op.reshape(3, 3))




"""Row1 , Row2, column = map (int, input().split())
array1 = [(list(map(int,input().split()))) for _ in range(Row1)]
array2 = [(list(map(int,input().split()))) for _ in range(Row2)]

print(np.concatenate((np.asarray(array1), np.asarray(array2)), axis = 0))"""


"""dim = tuple(map(int, input().split()))
print(np.zeros((dim), dtype= int))
print(np.ones((dim), dtype= int))


n, m = map (int, input().split())
array1 = [(list(map(int,input().split()))) for _ in range(n)]
array2 = [(list(map(int,input().split()))) for _ in range(n)]
array1 = numpy.asarray(array1)
array2 = numpy.asarray(array2)

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(numpy.floor_divide(array1, array2))
print(array1 % array2)
print(array1 ** array2)


n = int(input())
a = numpy.array([input().split() for _ in range(n)], float)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(a))"""



a = numpy.array(input().split(), float)
x = int(input())
numpy.set_printoptions(legacy='1.13')
print(numpy.polyval(a, x))