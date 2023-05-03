from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import requests
import json




# Get the HTML for the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_Shark_Tank_episodes'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
print('*')


# Get the season descriptions
table = soup.find('table',{'class':"wikitable plainrowheaders wikiepisodetable"}).tbody

rows = table.find_all('tr')

column_names = [v.text for v in rows[0].find_all('th')] # column names in the table : ['No.overall', 'No. inseason', 'Title', 'Original air date', 'Prod.code', 'U.S. viewers(millions)']
print(column_names)

df = pd.DataFrame(columns = column_names)


## TODO: Need to go over this again
for i in range(1, len(rows)):
    tds = rows[i].find_all('td')

    if len(tds) == 6:
        values = [tds[0].text, tds[1].text, '',tds[2].text,tds[3].text.replace('\n',''.replace('\xa0',''))]
    else:
        values = [td.text.replace('\n','').replace('\xa0','') for td in tds]

    df = df.append(pd.Series(values,index=column_names),ignore_index= True)
    print(df)
#
