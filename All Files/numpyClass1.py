import numpy as np
# ndim, shape, size
a = np.array([1, 2, 3, 4, 5])
a[3]
a.dtype
a.shape
a.size
a.ndim
a[3] = 10
# start:stop:step
a[0:5:3]
a[0:6] = 100, 200, 300, 400, 500 

u = np.array([4, 9])
v = np.array([5, 8])

z = u - v 
b = np.array([1.3, 6.7, 9, 90.0])

# mean, max, std_deviation, sum, subtract, multiply, divide, dot
c = np.random.randint(1, 50, 2)
x = np.random.randint(40, 50, 2)

# mean
c.mean()
x.mean()
# max
c.max()
x.max()
# 
c.std()
x.std()
# 
sum = c + x
np.sum(c, x)
sub = c- x
mult = x * c
div = x /c
np.dot(x,c)

# Two Dimension array
t = np.array([[3, 6, 8, 9, 1], [4, 5, 7, 10, 0]])
t.size
t.ndim
t.shape

t[1][3]
x = np.array([[3, 6, 8, 9, 1], [4, 5, 7, 10, 0]])
z = np.array([[4, 5, 7, 10, 0], [3, 6, 8, 9, 1]])

y = x / z
x.transpose()

print('hello','world', sep='-')
print('hello','world')
help(print)