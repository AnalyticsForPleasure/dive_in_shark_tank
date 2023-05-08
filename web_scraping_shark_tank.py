from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
import requests
import json



if __name__ == '__main__':

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    df = df[df['Entrepreneur Gender'] != 'Mixed Team']
    df = df.fillna(' ')
    print('*')

    #Add columns to dataframe to record Shark attendance
    shark_names = {'Mark': 'Cuban',
                   'Cuban': 'Mark',
                   'Kevin H.':'Harrington',
                   'Harrington':'Kevin H.',
                   'Daymond': 'John',
                   'John': 'Daymond',
                   'Barbara': 'Corcoran',
                   'Corcoran': 'Barbara',
                   'Robert': 'Herjavec',
                   'Herjavec': 'Robert',
                   'Kevin O.': "O'Leary",
                   "O'Leary": "Kevin O.",
                   'Lori': 'Greiner',
                   'Greiner': 'Lori',
                   }


# Adding 6 columns and filling the columns with zeros
    for val in shark_names.values():
        df[val+'_present'] = pd.Series(np.zeros(df.shape[0]), index=df.index) # added Zeros for each column which have 757 rows.
        df[val+'_present'] = np.random.randint(2, size = df.shape[0])
    print('*')

## Scrape the Wikipedia page
# Get the HTML for the Wikipedia page
#     url = 'https://en.wikipedia.org/w/index.php?title=List_of_Shark_Tank_episodes&oldid=911241643'
#     page = requests.get(url)
#     html = bs(page.text, 'html.parser')
#
#     # Get the season descriptions
#     seasons = html.find_all('table', class_="wikitable plainrowheaders wikiepisodetable") # still the same - don't change
#     print('*')
#
#     # num_season --> 1-10
#     # num_episode --> 1 - 25
#
#     num_season =3
#     for num_season,season in enumerate(seasons[:10]):
#
#         print("-"*30)
#         print("Season: {}".format(num_season+2))
#         #episodes = season.find_all('td', class_='description')
#         episodes = season.find_all('tr', class_='expand-child')
#         for num_episode,episode in enumerate(episodes):
#             # Determine which Sharks were on the episode
#             num_episode = 2
#             if num_season==0:
#                 sharks = ['Daymond','Kevin H.','Barbara','Robert','Kevin O.']
#             else: # Number of season 2-10
#                 sharks = episode.text.split('Sharks: ')[1].split('\n')[0].split(', ')
#                # For shark in sharks:
#                #     shark = shark.split(' ')[0]
#                 sharks = [shark.split(' ')[0] for shark in sharks]
#
#             # Update Shark attendance rates in the dataframe
#             mask_episode = (df['Season']==num_season+1) & (df['No. in series']==num_episode+1)
#             for shark in sharks:
#                 if shark in shark_names:
#                     df.loc[mask_episode, shark_names[shark]+'_present'] = 1
#
#         #df.sort_values(by = 'Season', inplace=True,ascending=False)
#         print('*')



sharks = ['Daymond','Kevin H.','Barbara','Robert','Kevin O.','Mark C.']
# The outer loop goes over and counts the number of male or Female presents to a specific shark (column )
for shark in sharks:
    print('-'*30)
    pitches = {'t': df[shark+"_present"].sum(),
               'f': df[df['Entrepreneur Gender']=='Female'][shark+"_present"].sum(),
               'm': df[df['Entrepreneur Gender']=='Male'][shark+"_present"].sum()}
    funded = {'t': 100*df[shark].sum()/df[shark+"_present"].sum()}
    for g in ['Female','Male']:
        mask = df[df['Entrepreneur Gender']==g] & (df[shark+"_present"]==1)
        funded[g[0].lower()] = 100*df[mask][shark].sum()/df[df.gender==g][shark+"_present"].sum()

    print("{s} was present for {t:.0f} pitches.".format(s=shark, t=pitches['t']))
    print("""\tPitches from women: {f:3.0f} ({pf:3.1f}%). Funded: {ff:3.1f}%
        Pitches from men: {m:5.0f} ({pm:3.1f}%). Funded: {fm:3.1f}%""".format(
        f=pitches['f'], pf=100*pitches['f']/pitches['t'], ff=funded['f'],
        m=pitches['m'], pm=100*pitches['m']/pitches['t'], fm=funded['m']))
