from std_operations import Add
from linalg import scalprod
a = -1
b = 3.14

c = Add(a,b)

print("{} + {} = {}".format(a,b,c))


u = np.array([1,0.5,-3.14])
v = np.array([-4,0,6.73])

udotv = scalprod(u,v)

print("{} dot {} = {}".format(u,v,udotv))
