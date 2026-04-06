import numpy as np
import sys

m, n = map(int, sys.stdin.readline().split(","))


A = []
for i in range(m):
    A.append(sys.stdin.readline().split(","))
A = np.array(A, dtype=int)


h, w = map(int, sys.stdin.readline().split(","))
pad_h = (h-1)//2
pad_w = (w-1)//2



pad_A = np.pad(A, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant')

C = []
for i in range(m):
    C.append(sys.stdin.readline().split(","))

C = np.array(C, dtype=int)

X = []
Y = []

for i in range(h):
    for j in range(w):
        part_A = pad_A[i: i+h, j: j+w]
        X.append(part_A.reshape(-1))
        Y.append(C[i, j])

B = np.round(np.flip(np.linalg.solve(X, Y).reshape(h, w))).astype(int)
#B = np.flip(np.round(np.linalg.lstsq(X, Y)[0].reshape(h, w)).astype(int))

for row in B:
    print(",".join(map(str, row)))