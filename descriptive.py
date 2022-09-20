import pandas as pd
import numpy as np
import math
import statistics
import scipy.stats
import matplotlib.pyplot as plt
from pandas import plotting
from statsmodels.formula.api import ols
import seaborn
from tableone import TableOne, load_dataset

####Using API link instead to reduce file size error

df = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')

###Data manipulation
df.shape
df.columns
df.dtypes

##Dataframe mean/variance/describe
df.mean()
df.var()
df.describe()

##Length of stay mean/variance/describe
df['length_of_stay'].mean()
df['length_of_stay'].var()
df['length_of_stay'].describe()


print(df['race'])

###Grouping to retrieve mean of length of stay per race
groupby_race = df.groupby('race')
for race, value in groupby_race['length_of_stay']:
    print((race,value.mean()))

###Plotting 
plotting.scatter_matrix(df[['ccs_diagnosis_code', 'ccs_procedure_code']])


###Histogram to view frequency of length of stay 
plt.style.use('ggplot')

hist, bin_edges = np.histogram(df['length_of_stay'], bins=10)
hist

bin_edges

fig, ax = plt.subplots()
ax.hist(df['length_of_stay'], bin_edges, cumulative=False)
ax.set_xlabel('Length_of_stay')
ax.set_ylabel('Frequency')
plt.show()


###Tableone

df_2 = df.copy()

df_2.dtypes

df_2.columns



df_2_columns = [['hospital_county', 'age_group', 'gender', 'race','type_of_admission','length_of_stay']]

df_2_columns


df_2_cat = [['age_group', 'gender']]

df_2_cat


df_2_group = ['gender']

df_2_group


df_2_sparcsdata = TableOne(df_2, columns=df_2_columns, categorical=df_2_cat, groupby=df_2_group, pval=False)
print(df_2_sparcsdata.tabulate(tablefmt="fancy_grid"))
df_2_sparcsdata.to_csv('SPARCS_2')

