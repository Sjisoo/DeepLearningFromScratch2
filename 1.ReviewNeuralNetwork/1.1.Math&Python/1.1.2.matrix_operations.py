import numpy as np

W = np.array([[1,2,3],[4,5,6]])
X = np.array([[0,1,2],[3,4,5]])

# 같은 위치의 원소끼리 연산

WplusX = W + X
print(WplusX)
'''
[[ 1  3  5]
 [ 7  9 11]]
'''

WmulX = W * X
print(WmulX)
'''
[[ 0  2  6]
 [12 20 30]]
'''