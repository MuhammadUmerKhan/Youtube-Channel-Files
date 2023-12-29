import pandas as pd
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
df = pd.read_csv(url)
df.head(8)
# Row, Column
df.iloc[1, 4]
df.iloc[1, 3]
df.loc[7, 'Rating']

df.loc[0:8, 'Released':'Released.1']