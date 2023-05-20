# TODO: Finish the circles
# 1. Get 10 most viewed episodes in each season
# 2. show it in a circle, each circle size presents the amount of viewers

import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
from bs4 import BeautifulSoup


# ******************************************************************************************************************
# Function  name: Part 1 -- "scraping_the_wiki_web_page_of_sark_tank_viewers"
# input:
# return value:
# ******************************************************************************************************************

def scraping_the_wiki_web_page_of_sark_tank_viewers(url):
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

    return df


# ******************************************************************************************************************
# Function  name: Part 2 -- "sciling_the_scraping_data_in_order_to_get_to_the_top_n_viewers_episode_in_aseason"
# input:
# return value:
# ******************************************************************************************************************

def scaling_the_scraped_data_in_order_to_get_to_the_top_n_viewers_episode_in_aseason(mini_df_season_number,season_number):
    # final_table = []
    # grouping_by_seasons = df.groupby('season')
    # for season_num, mini_df_season_num in grouping_by_seasons:
    # print(season_num)
    # print(mini_df_season_num)
    mini_df_season_num = mini_df_season_number.loc[mini_df_season_number['season'] == season_number, :]
    mini_df_season_num.sort_values(by='viewers', inplace=True, ascending=True)
    sorting_the_season_by_viewers = mini_df_season_num.sort_values(by='viewers')
    top_eight_episode = sorting_the_season_by_viewers.head(n=8)
    # Adding another column - "Percent" :
    top_eight_episode['Percent'] = [round(i * 100 / sum(top_eight_episode.viewers), 1) for i in
                                    top_eight_episode.viewers]
    top_eight_episode['Percent'] = (top_eight_episode['Percent']).apply(lambda x: "{0:.2f}".format(x)) + '%'
    # Adding "M" for the viewers:

    top_eight_episode['viewers'] = (top_eight_episode['viewers']).apply(lambda x: "{0:.2f}".format(x))  # +'M'
    top_eight_episode['viewers'] = top_eight_episode['viewers'].astype(float)
    # Adding X, Y coordinates scale :
    top_eight_episode['Y Position'] = [1] * len(top_eight_episode)
    list_x = list(range(0, len(top_eight_episode)))
    top_eight_episode['X Position'] = list_x

    top_eight_episode['episode'] = top_eight_episode['episode'].astype(str)

    top_eight_episode.dtypes
    print('*')

    return top_eight_episode


# ******************************************************************************************************************
# Function  name: Part 3 -- "visualizing_the_number_of_viewers_for_each_season_with_bubble_chart"
# input:
# return value:
# ******************************************************************************************************************
def visualizing_the_number_of_viewers_for_each_season_with_bubble_chart(top_eight_episode):
    pal_ = list(sns.color_palette(palette='crest', n_colors=len(top_eight_episode)).as_hex())
    # cmap = sns.color_palette("Blues", as_cmap=True).as_hex()
    # Now' let's go to the charting part:
    # create a labels list for each bubble
    label = [f'Episode {i} <br> {j} Million <br> {k}' for i, j, k in
             zip(top_eight_episode['episode'],
                 top_eight_episode['viewers'],
                 top_eight_episode['Percent'])]

    # Before passing the array of viewers into into the scatter plot we should
    # cast into float since it was string:
    # [3.56, 3.96 ,4.23, 4.3, 4.4, 4.44, 4.65, 4.79]
    # but the numbers are very close to each other, so we would like to rescale it using Exponential function:
    top_eight_episode['viewers'] = 50 ** top_eight_episode['viewers'].astype(float)

    # Now we got a better separation between the numbers so we will be able to see the difference sizes much more
    # clearly, output:
    # [1117720.497, 5344673.95, 15368911.80 , 20210218.95, 29886015.61, 34948361.49, 79471337.11, 137425181.99)

    fig = px.scatter(top_eight_episode,
                     x=list(top_eight_episode.loc[:, 'X Position']),
                     y=list(top_eight_episode.loc[:, 'Y Position']),
                     color=top_eight_episode['episode'],
                     color_discrete_sequence=pal_,
                     size=top_eight_episode['viewers'],
                     text=label,
                     size_max=50)
    fig.update_layout(width=900, height=320, margin=dict(t=50, l=0, r=0, b=0), showlegend=False)
    fig.update_traces(textposition='top center')
    fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_yaxes(showgrid=False, zeroline=False, visible=False)
    fig.update_layout({'plot_bgcolor': 'white',
                       'paper_bgcolor': 'white'})
    fig.show()
    print('*')


if __name__ == '__main__':
    # df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',
    #                    sheet_name='Sheet1')
    ########################################################################################################################
    # path 1 : retireiving the data from wiki web page:
    url = 'https://en.wikipedia.org/w/index.php?title=List_of_Shark_Tank_episodes&oldid=911241643'

    res = scraping_the_wiki_web_page_of_sark_tank_viewers(url)

    ########################################################################################################################
    # #Path 2 : Scaling the data of top 10 episodes viewer of each year


    # # creating dynamic Bubble Multi chart :
    groups_by_season = res.groupby('season')
    for season_number, mini_df_season_number in groups_by_season:
        res_2 = scaling_the_scraped_data_in_order_to_get_to_the_top_n_viewers_episode_in_aseason(mini_df_season_number,season_number)

    visualizing_the_number_of_viewers_for_each_season_with_bubble_chart(res_2)
    print('*')
    # # creating dynamic Waffle Multi chart :
    # df_all = creating_the_input_data_for_the_multi_whaffle_chart(df)
    # df_all.to_csv('whole_seasons.csv', index = False)
    # groups_by_season = df_all.groupby('season_number')
    # for season_number, mini_df_season_number in groups_by_season:
    #     generate_plot_per_season(mini_df_season_number, season_number)