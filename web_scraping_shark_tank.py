# TODO: Finish the circles
# 1. Get 10 most viewed episodes in each season
# 2. show it in a circle, each circle size presents the amount of viewers

import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import seaborn as sns

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

    final_table = []
    grouping_by_seasons = df.groupby('season')
    for season_num , mini_df_season_num in grouping_by_seasons:
        print(season_num)
        print(mini_df_season_num)
        mini_df_season_num.sort_values(by='viewers', inplace=True, ascending=True)
        sorting_the_season_by_viewers = mini_df_season_num.sort_values(by='viewers')
        top_eight_episode = sorting_the_season_by_viewers.head(n=8)

        # Adding another column - "Percent" :
        top_eight_episode['Percent'] = [round(i * 100 / sum(top_eight_episode.viewers), 1) for i in top_eight_episode.viewers]
        top_eight_episode['Percent'] = (top_eight_episode['Percent']).apply(lambda x: "{0:.2f}".format(x)) + '%'

        # Adding "M" for the viewers:
        top_eight_episode['viewers'] = (top_eight_episode['viewers']).apply(lambda x: "{0:.2f}".format(x)) +'M'

        # Adding X, Y coordinates scale :
        top_eight_episode['Y Position'] = [1]*len(top_eight_episode)
        list_x = list(range(0,len(top_eight_episode)))
        top_eight_episode['X Position'] = list_x


        top_eight_episode

        pal_ = list(sns.color_palette(palette='plasma_r', n_colors=len(top_eight_episode)).as_hex())

        #create a laebls list for each bubble
        label = [i+'/n'+str(j)+'/n'+str(k) for i,j,k in zip(top_eight_episode.episode,
                                                                    top_eight_episode.viewers,
                                                                    top_eight_episode.Percent)]

        fig = px.scatter(top_eight_episode, x='X Position', y='Y Position',
                         color='episode', color_discrete_sequence=pal_,
                         size='viewers', text=label, size_max=90)

        fig.update_layout(width=900, height=320,
                          margin = dict(t=50, l=0, r=0, b=0),
                          showlegend=False)
        fig.update_traces(textposition='top center')
        fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
        fig.update_yaxes(showgrid=False, zeroline=False, visible=False)
        fig.update_layout({'plot_bgcolor': 'white',
                           'paper_bgcolor': 'white'})
        fig.show()
    print('*')