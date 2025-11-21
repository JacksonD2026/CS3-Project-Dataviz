import pandas as pd
from matplotlib import pyplot as plt


plt.style.use('seaborn-v0_8-pastel')


df = pd.read_csv('ClassDataset2025 - class-dataset.csv')
df = df.head(8)
print(df.info())

birthYear = df['Birth Year']
birthDay = df['Birth Day']

plt.scatter(birthYear, birthDay)

plt.title('Birth Year VS Birth Day')
plt.xlabel('Birth Year')
plt.ylabel('Birth Day')
plt.axis('equal')

plt.savefig('scatter.png')
plt.close()



