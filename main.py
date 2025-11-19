import pandas as pd
from matplotlib import pyplot as plt


plt.style.use('seaborn-v0_8-pastel')


df = pd.read_csv('ClassDataset2025 - class-dataset.csv')
print(df.info())

birthYear = df['Birth Year']
birthDay = df['Birth Day']

plt.scatter(birthYear, birthDay)

plt.savefig('scatter.png')
plt.close()

