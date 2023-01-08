values = [0,0,1,1]
import numpy as np
index_min = np.argmin(values[2], values[3])

#index_min = min(values[2],values[3], key=values.__getitem__)

print(index_min)