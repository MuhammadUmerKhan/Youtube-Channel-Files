import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html')



# title = soup.title
table = soup.find_all('table')[0]
main_table = soup.find('table', class_ ="wikitable sortable")
titles = main_table.find('tr')

table_title = [title.text.strip() for title in titles]
table_titles = [sorted for sorted in table_title if sorted != '']
df = pd.DataFrame(columns = table_titles)

column_data = table.find_all('tr')
for row in column_data[2:]:
    row_data = row.find_all('td')
    individual_columns = [data.text.strip() for data in row_data]
    length =  len(df)
    # print(length)
    df.loc[length] = individual_columns
    
df.head()
df = df.drop(columns='State-owned', axis=1)
df.head()
len(df)

