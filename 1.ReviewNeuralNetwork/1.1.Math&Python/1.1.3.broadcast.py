import  numpy as np

A = np.array([[1,2],[3,4]])
broad = A * 10

print(broad)
'''
[[10 20]
 [30 40]]
 '''

b = np.array([10,20])
broad2 = A * b
print(broad2)
'''
[[10 40]
 [30 80]]
'''