import pandas as pd

####Using API link instead to reduce file size error

df = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')

df.shape
df.columns

print(df['hospital_county'])

