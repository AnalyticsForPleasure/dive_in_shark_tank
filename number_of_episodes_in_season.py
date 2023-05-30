import numpy as np
import pandas as pd
import dataframe_image as dfi
import matplotlib.pyplot as plt

# **************************************************************************************************************
# Function  name: get_number_of_investments_each_season_over_the_years
# input:
# return value:
# ****************************************************************************************************************
def get_number_of_investments_each_season_over_the_years(df):
    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    res = all_the_deals_closed['Season'].value_counts().to_frame()
    res = res.reset_index(level=0)
    res.rename(columns={res.columns[0]: 'season_number'}, inplace=True)
    res.rename(columns={res.columns[1]: 'Amount_of_investments_over_each_season'}, inplace=True)
    res['season_number'] = res['season_number'].apply(lambda x: int(x))
    res.sort_values(by='season_number', inplace=True, ascending=True)
    dfi.export(res,'result_investment_per_season.png')
    print('*')

    return res
# **************************************************************************************************************
# Function  name: creating a gradient area bar for the number of investments made during the seasons
# input:
# return value:
# ****************************************************************************************************************
def creating_gradient_area_bar_chart_for_the_investments_over_the_seasons(table):
    print('*')
    number_of_season = list(table.iloc[:,'season_number'])
    number_of_investments_over_each_season = list(table.iloc[:,'number_of_investments_over_each_season'])
    plt.fill_between(number_of_season,#np.arange(10)+1,
                     number_of_investments_over_each_season,
                     color="skyblue",
                     alpha=0.4)
    plt.plot(np.arange(10)+1,
             number_of_investments_over_each_season,
             color="Slateblue",
             alpha=0.6,
             linewidth=2)
    plt.tick_params(labelsize=12)
    plt.xticks(np.arange(10)+1, np.arange(10)+1)
    plt.xlabel('Season Number', size=17)
    plt.ylabel('Number of Investments made over each season', size=17)
    plt.ylim(bottom=0)


if __name__ == '__main__':
    pd.set_option('display.max_rows', 900)

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')  # Ten seasons


    my_result =get_number_of_investments_each_season_over_the_years(df)
    creating_gradient_area_bar_chart_for_the_investments_over_the_seasons(my_result)
    print('*')





