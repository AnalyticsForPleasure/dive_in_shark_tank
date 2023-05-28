import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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
    shark_table.to_csv('part_one_3d.csv', index = False)
    print('*')
    return shark_table

# ******************************************************************************************************************
# Function  name: creating_the_data_for_the_3d_plot
# input:
# return value:
# ******************************************************************************************************************

def creating_the_3D_chart(df):
    data = pd.read_csv('C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/part_one_3d.csv')
    data = data.set_index('Industry')
    res = data.to_numpy()

    shark_names = ['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond', 'Kevin']
    industries_names = ['Health', 'Food', 'LifeStyle', 'Children','Fashion','Business Services',
                        'Fitness','Pet Products','Tech','Media','Travel','CleanTech','Autoemotive','Other' ]

    number_of_industries = 5

    df = pd.DataFrame(data=res[:number_of_industries],#actual_bar_heights,
                      columns=shark_names,
                      index=industries_names[:number_of_industries])
    res = df.to_numpy()
    print('*')
    # The coordinates of the anchor point of the bars:

    x = [idx + 0.5 for idx, _ in enumerate(shark_names, start=1)]
    y = [idx + 0.5 for idx, _ in enumerate(industries_names[:number_of_industries], start=1)]

    xx, yy = np.meshgrid(x, y)

    xx = xx.flatten()
    yy = yy.flatten()
    zz = [0] * len(industries_names[:number_of_industries]) * len(shark_names)

    colors = sorted(['skyblue', 'dodgerblue', 'lightseagreen','palegreen','navy'] * len(shark_names)) # 'lightsteelblue', 'black']

    # dx, dy, dz : float or array-like
    # The width, depth, and height of the bars, respectively:
    bar_width = 0.05
    bar_depth = 0.4

    width_vec = [bar_width] * len(xx)
    depth_vec = [bar_depth] * len(yy)
    heights_vec = res.flatten()

    plt.figure(figsize=(0, 12))
    ax = plt.axes(projection='3d')
    ax.bar3d(x=xx - bar_width / 2,
             y=yy - bar_depth / 2,
             z=zz,
             dx=width_vec,
             dy=depth_vec,
             dz=heights_vec,
             color=colors)

    ax.xaxis.set_ticks(x)
    ax.set_xticklabels(shark_names)
    ax.yaxis.set_ticks(y)
    ax.set_yticklabels(industries_names[:number_of_industries])

    ax.set_xlabel("Shark Name", labelpad=12)
    ax.set_ylabel("Industry name", labelpad=12)
    ax.set_zlabel("Number of times invested", labelpad=12)

    ax.set_title("Investments per Industry per shark")
    plt.show()


if __name__ == '__main__':


    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    print('*')

    res = creating_the_data_for_the_3d_plot(df)
    creating_the_3D_chart(res)
    print('*')