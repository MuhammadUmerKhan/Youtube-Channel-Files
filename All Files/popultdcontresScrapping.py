import pandas as pd
from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/World_population"
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
title = soup.title.text

tables = soup.find_all('table')
dataFrame = []
for i, table in enumerate(tables):
    row = table.find_all('tr')[1:]
    data = []
    for col in row:
        cols = col.find_all('td')
        cols = [rows.text.strip() for rows in cols]
        data.append(cols)
    df = pd.DataFrame(data)
    dataFrame.append(df)
dataFrame[0]
