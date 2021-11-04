import numpy as np


a=np.array([1,2,3,4])
b = np.array([5,5,5,5])



a+b # element-wise product



np.dot(a,b) #dot-product

c = np.array([1,2,3])

# b * c # error! dimensions mismatched


# 2-dim arrays

a = np.array([[1,2,3,4],[5,6,7,8]])
b = np.array([[5,5,5,5]])

np.dot(a,b.T)
np.zeros((3,4))
np.ones((3,4))


rands = np.random.random(size = 100)


k = [int(x) for x in (np.random.random(size = 100) * 6)] #均匀分布create random integer between 0~6

# [int(x) + 1 for x in (np.random.random(size = 100) * 6)]
# [int(x) for x in (np.random.random(size = 100) * 6 + 1)]


np.random.standard_normal()
np.random.standard_normal(size = 100) #生成正态分布随机数


# we don't "append" to an np.array
# instead, create an array of zeros and assig

x = np.zeros(10)

x[0] = 1
x[1] = 42




 

































