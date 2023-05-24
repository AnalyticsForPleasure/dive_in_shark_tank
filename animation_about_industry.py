import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt


# ******************************************************************************************************************
# Function  name: creating_the_data_for_the_3d_plot
# input:
# return value:
# ******************************************************************************************************************
def creating_the_data_for_the_3d_plot(df):

    list_of_sharks = ['Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn',
                      "Kevin\nO'Leary"]
    unique_industries = df['Industry'].unique()
    shark_table = pd.DataFrame({'Industry': unique_industries,
                                'Counter_shark': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]})

    for shark_name in list_of_sharks:
        investment_made_by_shark = df.loc[df[shark_name] == 1, :]
        res = investment_made_by_shark['Industry'].value_counts()
        result = res.reset_index(level=0)
        result.rename(columns={result.columns[1]: f'{shark_name}'}, inplace=True)
        result.columns = result.columns.str.replace('\n', '')


        result.rename(columns={result.columns[0]: 'Industry'}, inplace=True)

        # Merge shark_table with result
        shark_table = pd.merge(shark_table, result, on='Industry', how='left')
        print('*')
    print(shark_table)
    shark_table = shark_table.drop(['Counter_shark'], axis=1)  # drop column named --> "Counter_shark"
    shark_table.fillna(0, inplace=True)  # Replace NA values with zeros
    shark_table.iloc[:, 1:7] = shark_table.iloc[:, 1:7].apply(lambda x: x.astype(int))
    shark_table.drop(0, axis=0, inplace=True)  # remove the first row
    dfi.export(shark_table, 'shark_table.png')
    print('*')


# ******************************************************************************************************************
# Function  name: creating_the_data_for_the_3d_plot
# input:
# return value:
# ******************************************************************************************************************

    df = pd.read_csv("sample_datasets/auto_clean.csv")

    print(np.unique(df['body-style']))

    df['body-style1'] = df['body-style'].replace({'convertible': 1,
                                                  'hardtop': 2,
                                                  'hatchback': 3,
                                                  'sedan': 4,
                                                  'wagon': 5
                                                  })

    gr = df.groupby("body-style1")["city-mpg", "price"].agg('median')

    x = gr.index
    y = gr['city-mpg']
    z = [0] * 5

    colors = ['skyblue', 'g', 'r', 'pink', 'coral']

    dx = [0.3] * 5
    dy = [1] * 5
    dz = gr['price']  # Number of investments for category

    plt.figure(figsize=(0, 12))
    ax = plt.axes(projection='3d')
    ax.bar3d(x, y, z, dx, dy, dz, color=colors)
    #ax.set_xticklabels(['convertible', 'hardtop', 'hatchback', 'sedan', 'wagon'])
    ax.set_xticklabels(['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond',"Kevin"])

    ax.set_xlim(0, 5.5)
    ax.set_xlabel("shark names", labelpad=12)
    ax.set_ylabel("Categories", labelpad=12)
    ax.set_zlabel("Number of investments", labelpad=12)
    ax.set_title("Number of investments by categories")
    plt.show()


if __name__ == '__main__':


    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    print('*')

    creating_the_data_for_the_3d_plot(df)
    print('*')