import pandas as pd
import dataframe_image as dfi

if __name__ == '__main__':


    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    print('*')

    list_of_sharks = ['Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary"]
    #
    # unique_industries=df['Industry'].unique()
    # shark_table =pd.DataFrame({'Industry':[unique_industries],
    #                            'Counter_shark':[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]})
    #
    #
    # print('*')
    #
    # for shark_name in list_of_sharks :
    #     investment_made_by_shark = df.loc[df[shark_name]== 1,:]
    #     res= investment_made_by_shark['Industry'].value_counts()
    #     result = res.reset_index(level=0)
    #     result.rename(columns={result.columns[1]: f'Counter_{shark_name}'},inplace=True)
    #     result.rename(columns={result.columns[0]: 'Industry'}, inplace=True)
    #
    #     #merged_result = pd.merge(result, shark_table, on='Industry', how='inner')
    #     print('*')
    #
    #
    # print('*')


#column_headers = list(df.columns.values) 'Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary",

    unique_industries = df['Industry'].unique()
    shark_table = pd.DataFrame({'Industry': unique_industries,
                                'Counter_shark': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})

    print('*')

    for shark_name in list_of_sharks:
        investment_made_by_shark = df.loc[df[shark_name] == 1, :]
        res = investment_made_by_shark['Industry'].value_counts()
        result = res.reset_index(level=0)
        result.rename(columns={result.columns[1]: f'Counter_{shark_name}'}, inplace=True)
        result.rename(columns={result.columns[0]: 'Industry'}, inplace=True)

        # Merge shark_table with result
        shark_table = pd.merge(shark_table, result, on='Industry', how='left')
        print('*')
    print(shark_table)

    shark_table=shark_table.drop(['Counter_shark'], axis=1) # drop column named --> "Counter_shark"
    shark_table.fillna(0, inplace=True) # Replace NA values with zeros
    shark_table.iloc[:, 1:7] = shark_table.iloc[:, 1:7].apply(lambda x: x.astype(int))
    shark_table.drop(0,axis=0,inplace=True)# remove the first row

    dfi.export(shark_table, 'shark_table.png')

    print('*')