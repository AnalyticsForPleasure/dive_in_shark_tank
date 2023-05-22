import pandas as pd

if __name__ == '__main__':


    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    print('*')

    list_of_sharks = ['Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary"]

    unique_industries=df['Industry'].unique()
    shark_table =pd.DataFrame({'Industry':[unique_industries],
                               'Counter_shark':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})


    print('*')

    for shark_name in list_of_sharks :
        investment_made_by_shark = df.loc[df[shark_name]== 1,:]
        res= investment_made_by_shark['Industry'].value_counts()
        result = res.reset_index(level=0)
        result.rename(columns={result.columns[1]: f'Counter_{shark_name}'},inplace=True)
        result.rename(columns={result.columns[0]: 'Industry'}, inplace=True)

        #merged_result = pd.merge(result, shark_table, on='Industry', how='inner')
        print('*')


    print('*')


#column_headers = list(df.columns.values) 'Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary",