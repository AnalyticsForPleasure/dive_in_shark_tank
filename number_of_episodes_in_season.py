import numpy as np
import pandas as pd
import dataframe_image as dfi

# **************************************************************************************************************
# Function  name: get_number_of_investments_each_season_over_the_years
# input:
# return value:
# ****************************************************************************************************************




if __name__ == '__main__':
    pd.set_option('display.max_rows', 900)

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')  # Ten seasons
    print('*')




#def get_number_of_investments_each_season_over_the_years(all_the_deals_closed):
    res = all_the_deals_closed['Season'].value_counts().to_frame()
    res = res.reset_index(level=0)
    res.rename(columns={res.columns[0]: 'season_number'}, inplace=True)
    res.rename(columns={res.columns[1]: 'amount_of_investments_over_each_season'}, inplace=True)
    #res['season_number'] = res['season_number'].astype(str) + ' season'  # adding a string into specific column
    print('*')

    return res
