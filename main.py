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

plt.savefig('birt.png')
plt.close()

Jewish = df['Jewish']
Flavor = df['Flavor']

plt.scatter(Jewish, Flavor)

plt.title('Jewish VS Flavor')
plt.xlabel('Jewish')
plt.ylabel('Flavor')
plt.axis('equal')

plt.savefig('scatter.png')
plt.close()


Years_At_BWL = df['Years at BWL']
B5_Openness = df['BigFive Openness']

plt.scatter(Years_At_BWL, B5_Openness)
plt.title('How open does BWL make you?')
plt.xlabel('Years at BWL')
plt.ylabel('BigFive Openness')
plt.axis('equal')

plt.savefig('bwlopening.png')
plt.close()



