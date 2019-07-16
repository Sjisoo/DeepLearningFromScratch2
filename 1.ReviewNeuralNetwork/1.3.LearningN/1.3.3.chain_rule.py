import numpy as np
D, N = 8, 7

# input
x = np.random.rand(1, D)

### forward
# x 배열을 N번 복
y = np.repeat(x, N, axis=0)

# 무작위 기울기
dy = np.random.rand(N, D)

### back
dx = np.sum(dy, axis=0, keepdims=True)

print(x)

# sum
# x = np.random.rand(N,D)
# y = np.sum(x, axis=0, keepdims=True)

# dy = np.random.rand(1, D)
# dx = np.repeat(dy, N, axis=0)


