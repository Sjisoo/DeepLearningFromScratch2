import  numpy as np

class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, params, grads):
        for i in range(len(params)):
            params[i] -= self.lr * grads[i]


#optimizer = SGD()

#for i in range(10000):
#    ...
#    optimizer.update(model.params, model.grads)
#    ...