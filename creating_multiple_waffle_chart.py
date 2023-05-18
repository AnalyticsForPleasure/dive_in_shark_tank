import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pywaffle import Waffle

# ******************************************************************************************************************
# Function  name: Helper function  - convert_to_number
# input:
# return value:
# ******************************************************************************************************************
def convert_to_number(text_row):
    if text_row is np.nan:
        return 0

    value_cap = text_row.replace('$', '').replace(',', '')

    return value_cap


# ******************************************************************************************************************
# Function  name: Helper function convert_percentage_number
# input:
# return value:
# ******************************************************************************************************************
def convert_percentage_number(text_row):
    if text_row is np.nan:
        return 0
    percentage_number = float(text_row.replace('%', ''))
    return percentage_number


# ******************************************************************************************************************
# Function  name: creating_the_input_data_for_the_multi_whaffle_chart
# input:
# return value:
# ******************************************************************************************************************
def creating_the_input_data_for_the_multi_whaffle_chart(df):
    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    all_the_deals_closed = all_the_deals_closed.replace(np.nan, '', regex=True)
    print('*')
    all_the_deals_closed['Close_DEAL'] = all_the_deals_closed['DEAL_Amount'].apply(lambda x: convert_to_number(x))
    all_the_deals_closed = all_the_deals_closed.loc[all_the_deals_closed['Close_DEAL'] != '', :]
    all_the_deals_closed['Close_DEAL'] = all_the_deals_closed['Close_DEAL'].astype('int')

    list_of_seasons = []
    df_shark = pd.DataFrame({'Investor_name': [],
                             'Amount_of_investments': [],
                             'Percent': [],
                             'season_number': []
                             })

    groups_by_season = all_the_deals_closed.groupby('Season')
    for season_number, mini_df_season_number in groups_by_season:
        # print(f'Season #{season_number}')
        mini_df_season_number.reset_index(inplace=True, drop=True)
        investors_matrix = mini_df_season_number.iloc[:, 17:24]
        investors_matrix = investors_matrix.replace('', 0)
        investors_matrix = investors_matrix.astype('int')
        mini_df_season_number['number_of_investors'] = investors_matrix.sum(axis=1)
        mini_df_season_number['investment_per_investor'] = mini_df_season_number['Close_DEAL'] / \
                                                           mini_df_season_number['number_of_investors']

        infinite_investment = mini_df_season_number['investment_per_investor'] == np.inf
        mini_df_season_number.loc[infinite_investment, 'investment_per_investor'] = 0
        # Here below we used the multiply function taken from numpy
        res = np.multiply(investors_matrix.T,
                          mini_df_season_number['investment_per_investor'])
        res2 = res.sum(axis=1).to_frame()  # In order to convert from series to dataframe I used use to_frame()
        res2.reset_index(level=0, inplace=True)
        res2.rename(columns={res2.columns[0]: 'Investor_name'}, inplace=True)
        res2.rename(columns={res2.columns[1]: 'Amount_of_investments'}, inplace=True)
        res2['Amount_of_investments']=res2['Amount_of_investments'].apply(lambda x:int(x))
        # Adding another column - "Percent" :
        res2['Percent'] = [round(i * 100 / sum(res2.Amount_of_investments), 1) for i in res2.Amount_of_investments]
        res2['Percent'] = (res2['Percent']).apply(lambda x: "{0:.2f}".format(x))   + '%'
        # Adding another column - "season_number" :
        res2['season_number'] = season_number
        dfi.export(res2, 'multi_whaffle_10.png')

        print(f'Season #{season_number}:\n {res2}')
        df_shark['Investor_name'] = df_shark['Investor_name'].apply(lambda x: x.replace('\n', ' '))
        df_shark = pd.concat([df_shark, res2], axis=0)
        df_shark['season_number'] = df_shark['season_number'].apply(lambda x: int(x))
        print('*' * 50)
    # In the next row we will export data into CSV
    # df_shark.to_csv(fr'C:\Users\Gil\PycharmProjects\building-blocks-python\Coding_in_finance\shark_output\{season_number}.csv', index = False)

    return df_shark


# ******************************************************************************************************************
# Function  name: generate_plot_per_season
# input:
# return value:
# ******************************************************************************************************************
def generate_plot_per_season(mini_df_season_number, season_number):
    dict_subplots_data = dict()
    number_of_images = [6] * 6
    col_number = [1] * 6
    total_squares = 100
    rows = list(range(1, 7))

    pal = list(sns.color_palette(palette='plasma_r', n_colors=len(mini_df_season_number.Investor_name)).as_hex())
    # Loop for creating dictionary
    for number_image, col, row, per, investor_name, color in zip(number_of_images,
                                                                 col_number,
                                                                 rows,
                                                                 mini_df_season_number['Percent'],
                                                                 mini_df_season_number['Investor_name'],
                                                                 pal):
        current_k = number_image * 100 + col * 10 + row

        dict_subplots_data[current_k] = {
            'values': {'Cat1': int(float(per)), 'Rest': total_squares - int(float(per))},
            'labels': [investor_name + ' ' + str(per) + ' %',
                       'Rest of the sharks' + ' ' + str(100 - float(per)) + ' %'],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 8},
            'title': {'label': f'{investor_name}' ' invesments', 'loc': 'left', 'fontsize': 12},
            'colors': [color, "#EEEEEE"]
        }

    fig = plt.figure(
        FigureClass=Waffle,
        plots=dict_subplots_data,
        rows=5,  # Outside parameter applied to all subplots, same as below
        cmap_name="Accent",  # Change color with cmap
        rounding_rule='ceil',  # Change rounding rule, so value less than 1000 will still have at least 1 block
        figsize=(12, 5)
    )

    fig.suptitle(f'Season {season_number}', fontsize=14, fontweight='bold')
    fig.supxlabel('Each square present 1% of the investments made by the total group of sharks', fontsize=8, x=0.36,
                  style='italic')
    fig.set_facecolor('#ffffff')
    # plt.savefig(f'{waffle_season_1[:-4]}.jpg', dpi=250)
    plt.savefig(f'waffle_{season_number}_2.jpg', dpi=250, bbox_inches='tight')


plt.show()



if __name__ == '__main__':

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')

    # creating dynamic Waffle Multi chart :
    df_all = creating_the_input_data_for_the_multi_whaffle_chart(df)
    df_all.to_csv('whole_seasons.csv', index = False)
    groups_by_season = df_all.groupby('season_number')
    for season_number, mini_df_season_number in groups_by_season:
        generate_plot_per_season(mini_df_season_number, season_number)
    print('*')