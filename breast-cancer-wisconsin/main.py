import pandas as pd

path = r'./breast-cancer-wisconsin.csv'
df = pd.read_csv(path, index_col='id')

df = df.replace('B', 0)
df = df.replace('M', 1)


df.to_csv(path_or_buf=r'./breast-cancer-wisconsin-adapter.csv',
          header=None, index=False)
