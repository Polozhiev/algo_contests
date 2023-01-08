import numpy as np

def IIR_filter(x, alpha=0.5):
    # alpha - weight for reccurent connection
    
    y = np.zeros_like(x, dtype=np.float64)
    t = 0
    
    for i in range(y.shape[0]):
        y[i] += t * (alpha) + x[i]
        t = y[i]

    return y


x =[1, 2, 3, 4, 5, 6, 12, 8, 9]
y = IIR_filter(x)
print(y)

