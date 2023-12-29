from bs4 import BeautifulSoup
import requests 
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')
# print(soup.prettify())
# print(soup.title.text)
# print(soup)
# tag_child = soup.b

# tag_child = tag_child.parent
# tag_child = tag_child.next_sibling
# print(tag_child)
# print(tag_child.get('id'))
# print(tag_child.text)

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
findTable = two_tables_bs.find("table")
print(two_tables_bs.find("table",class_='pizza'))
# print(two_tables_bs.prettify())
# print(findTable)
url = "http://www.ibm.com"
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html5lib") 
print(soup.prettify())


for link in soup.find_all('a',href=True):

    print(link.get('href'))
    
for img in soup.find_all('img'):
    print(img.text)
    print(img.get('src'))


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
data  = requests.get(url).text
soup = BeautifulSoup(data, 'html5lib')
# print(soup.prettify())
print(soup.h1.text)
tables = soup.find('table')
print(tables[0])
table_col = tables.find('tr')
cols = [table_col.text.strip() for col in table_col]

for row in tables.find_all('tr'):
    cols = row.find_all('td') 
    color_name = cols[2].string
    color_code = cols[3].text 
    print("{}--->{}".format(color_name,color_code))
    