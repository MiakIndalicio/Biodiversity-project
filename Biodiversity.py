#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('E:\Cody\Documents\\BiodiversityStarter\\biodiversity_starter\\observations.csv')
# print(data.head())
data2 = pd.read_csv('E:\Cody\Documents\\BiodiversityStarter\\biodiversity_starter\\species_info.csv')
# print(data2.head())

# sns.histplot(x = data['observations'])
# plt.show()
# plt.clf()

plt.bar(data['park_name'], data['observations'], color = 'blue', width = 0.5)
plt.xticks(rotation = 30, fontsize = 8)
plt.xlabel('Park Name')
plt.ylabel('Observations')
plt.title('Observations Based on Parks')
plt.show()
plt.clf()

sns.countplot(data = data2, x = data2['category'])
plt.xticks(rotation = 90, fontsize = 6)
plt.xlabel('Species Type')
plt.show()
plt.clf
category_counts = data2['category'].value_counts()
print(category_counts)

sns.countplot(data = data2, x = data2['conservation_status'])
plt.show()
plt.clf()
conservation_counts = data2['conservation_status'].value_counts()
print(conservation_counts)
total = data2.stack().value_counts()
naan_counts = total - conservation_counts
print(naan_counts)

sns.countplot(data = data2, x = data2['conservation_status'], hue = data2['category'])
plt.show()
plt.clf()



sns.countplot(x = data2['conservation_status'], hue = data['scientific_name'])
plt.show()
plt.clf()


endangered_birds = data2[(data2['category'] == 'Bird') & (data2['conservation_status'] == 'Endangered')]

# Extract common names of endangered bird species
bird_names = endangered_birds['common_names']

# Create a count plot
plt.figure(figsize=(10, 6))
sns.countplot(data=endangered_birds, x='common_names', palette='Set2')
plt.xlabel('Bird Species')
plt.ylabel('Count')
plt.title('Endangered Bird Species')
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()