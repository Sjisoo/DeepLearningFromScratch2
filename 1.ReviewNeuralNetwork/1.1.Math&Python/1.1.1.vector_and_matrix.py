import numpy as np

x = np.array([1, 2, 3])
x.__class__
x.shape
x.ndim

print(x.__class__)
print(x.shape)
print(x.ndim)
'''
<class 'numpy.ndarray'>
(3,)
1
'''

W = np.array([[1,2,3],[4,5,6]])
W.shape
W.ndim

print(W.__class__)
print(W.shape)
print(W.ndim)
'''
<class 'numpy.ndarray'>
(2, 3)
2
'''