import cuda_runtime as cr
import cupy as cp
import numpy as np

cp1 = cp.arange(4, dtype=cp.float32)
print(cp1)

t1 = cr.malloc(16)
cr.memcpy(t1, cp1.data.ptr, 16, 3)

cp2 = cp.zeros(4, dtype=cp.float32)
print(cp2)
cr.memcpy(cp2.data.ptr, t1, 16, 3)
print(cp2)








