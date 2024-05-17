import numpy as np
a = np.array([[5 ,6, 9] , [1 ,2 ,3] ], dtype=complex)
print(a[0])
print(a.ndim)
print(a.itemsize)
print(a.size)
print(a.shape)
print(a)
b = np.zeros((3,2))
print(b)
l = range(5)
print(l)
c = np.arange(1,5)
print(c)
d = np.arange(1 , 5 ,2)
e = np.linspace(1, 5 ,200)
m = b.reshape(2 ,3)
print(e)

f = b.ravel()
print(f)
print(m)


z = a.min()
y = a.max()

#axis0 -> colummn
#axis1 ->  rows

a.sum(axis=0)
a.sum(axis=1)

np.sqrt(a)
np.std(a)
a = np.array([[1,2] ,[3,4]])
b = np.array([[2 ,3],[5,6]])
d =a+b
d= a*b
d= a/b
a.dot(b)