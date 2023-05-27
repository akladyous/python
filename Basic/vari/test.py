import numpy as np
import pandas as pd

d = {'x1': [1, 4, 4, 5, 6],
     'x2': [0, 0, 8, 2, 4],
     'x3': [2, 8, 8, 10, 12],
     'x4': [-1, -4, -4, -4, -5]}
df = pd.DataFrame(data = d)

pairs_to_drop = set()
cols = df.columns

dfs=df.shape[1]

for i in range(0, df.shape[1]):
    for j in range(0, i+1):
        pairs_to_drop.add((cols[i], cols[j]))

print(pairs_to_drop)
