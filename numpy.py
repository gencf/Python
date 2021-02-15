import numpy as np
a = np.array([[1, 2],
              [4, 5]])

b = np.array([[7, 8],
              [10,11]])

c= np.array([[1,2,3,4,5,6],
            [7,8,9,10,11,12],
            [13,14,15,16,17,18]])
d = c[:2,:2]
A = np.array([[2,3,4],
              [5,-6,7],
              [8,9,10]])
result = [119,80,353]

s = np.array([[2,3,-1],
              [-1,-1,1],
              [3,-1,-1]])
r = np.array([5, 0, -2])
print("solve s:",np.linalg.solve(s,r), np.linalg.inv(s) @ r, np.linalg.inv(s) @ r.T)

print("a:\n", a, "\nb:", b, "\nc:\n", c, "\nd:\n", d)
print("a.shape:\n", a.shape, "\nb.shape:\n", b.shape, "\nc.shape:\n", c.shape)
print("c[1:3,(1,4)]:\n", c[1:3,(1,4)])
print("c[1,(3,5):\n",c[1,(3,5)])
print("c[(1,2),(3,4)]:\n", c[(1,2),(3,4)])
d[:] = np.zeros((2,2))
print("d:\n", d, "\nc:\n", c)
print("np.ones(3):\n", np.ones((2,4,3)))
x = np.linalg.solve(A, result)
print("A:\n", A, "\nresult:\n", result, "\nsolution:\n", x)
print("result:\n", A @ x.T, A @ x, np.inner(A, x))
print()
print("a:\n", a, "\nb:\n", b, "\nc:\n", c)
print("a*b:\n",a*b)
print("a@b:\n",a@b)
print("a.dot(b):\n",a.dot(b))
print("\nnp.inner(a,b):\n", np.inner(a,b), "\na.dot(b.T):\n", a.dot(b.T))
print("np.outer(a,b):\n", np.outer(a,b))
print("np.cross(a,b):\n", np.cross(a,b)),
print("np.cross(a,b):\n", np.cross(b,a))
print("a.T:\n", a.T, "\nb.T:\n", b.T)
print("np.sum(a, axis=1):\n", np.sum(a, axis=1))
print(np.sum(np.sum(a, axis = 0) > [5,6]))
