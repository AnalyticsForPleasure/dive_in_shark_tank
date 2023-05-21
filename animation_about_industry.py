import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataframe_image as dfi




if __name__ == '__main__':


    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    print('*')

    list_of_sharks = ['Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary"]


    for shark_name in list_of_sharks :
        investment_made_by_shark = df.loc[df[shark_name]== 1,:]
        res= investment_made_by_shark['Industry'].value_counts()
        #result =res.rename(columns={res[0]: res.index[0]},inplace=False)
        res = res.rename({res.index[0]: f'{shark_name}'}, inplace=True) #TODO need to work on this line
        print('*')


#column_headers = list(df.columns.values) 'Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary",