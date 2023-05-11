# TODO: Finish the circles
# 1. Get 10 most viewed episodes in each season
# 2. show it in a circle, each circle size presents the amount of viewers

import pandas as pd
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',
                       sheet_name='Sheet1')
########################################################################################################################
    #path 1 : retireiving the data from wiki web page:

    # Scrape the Wikipedia page
    # Get the HTML for the Wikipedia page
    url = 'https://en.wikipedia.org/w/index.php?title=List_of_Shark_Tank_episodes&oldid=911241643'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    all_tables = soup.findAll('table', attrs={'class': 'wikitable plainrowheaders wikiepisodetable'})
    episode_number_list = []
    season_number_list = []
    num_viewers_list = []
    for season_number, current_table in enumerate(all_tables[:-1], start=1):

        all_episodes = current_table.findAll('tr', attrs={'class': 'vevent'})
        if season_number < 10:
            print(f'season_number = {season_number}')
            for episode_number, row in enumerate(all_episodes, start=1):
                # The rating is appears in the last column:
                num_viewers = row.contents[-1].text
                if num_viewers.find('[') != -1:
                    num_viewers = num_viewers[:num_viewers.find('[')]
                # print(num_viewers)
                episode_number_list.append(episode_number)

                try:
                    num_viewers = float(num_viewers)
                    num_viewers_list.append(num_viewers)
                except Exception as e:
                    problematic_index = len(num_viewers_list)
                    print(e)
        else:
            # in the last table the rating appears before the last column:
            for episode_number, row in enumerate(all_episodes, start=1):
                num_viewers = row.contents[-2].text
                # In next row tells we can't find "[" , then it will gives as (-1)
                if num_viewers.find('[') != -1:
                    num_viewers = num_viewers[:num_viewers.find('[')]
                episode_number_list.append(episode_number)
                # print(num_viewers)

                try:
                    num_viewers = float(num_viewers)
                    num_viewers_list.append(num_viewers)
                except Exception as e:
                    problematic_index = len(num_viewers_list)
                    print(e)

        season_number_list += len(all_episodes) * [season_number]

    num_viewers_list = num_viewers_list[:problematic_index] + [6.15] + num_viewers_list[problematic_index:]

    data_dict = {"season": season_number_list,
                 "episode": episode_number_list,
                 "viewers": num_viewers_list
                 }

    df = pd.DataFrame(data_dict)
    print(*'')
########################################################################################################################
# #Path 2 : Scaling the data of top 10 episodes viewer of each year