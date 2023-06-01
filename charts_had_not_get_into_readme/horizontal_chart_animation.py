import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
from bs4 import BeautifulSoup
import kaleido
import dataframe_image as dfi
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


if __name__ == '__main__':

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    df_2 = pd.read_csv('/Data/shark_tank_companies.csv')  # six seasons
    column_headers = list(df.columns.values)

    #res =df.loc['State']
    #df = df.rename(index={'Unnamed: 8': 'state'})
    df = df.rename(index={'8': 'state'})
    print('*')

    all_the_deals_closed = df.loc[df['Deal'] == 'Yes',:]
    all_the_deals_closed = all_the_deals_closed.replace(np.nan, '', regex=True)


    gender_table =pd.DataFrame({'shark_name':[]})

    groups_by_gender = all_the_deals_closed.groupby('Entrepreneur Gender')
    for gender, mini_df_gender in groups_by_gender:
        mini_df_gender.reset_index(inplace=True, drop=True)
        gender_table_matrix = mini_df_gender.loc[:, 'Barbara\nCorcoran':"Kevin\nO'Leary"]
        gender_table_matrix = gender_table_matrix.replace('', 0)
        gender_table_matrix = gender_table_matrix.astype('int')
        gender_table_matrix = gender_table_matrix.sum()
        gender_table_matrix = gender_table_matrix.reset_index(level=0)
        gender_table_matrix.rename(columns={gender_table_matrix.columns[0]: 'shark_name'}, inplace=True)
        gender_table_matrix.rename(columns={gender_table_matrix.columns[1]: f'{gender}'}, inplace=True)

        current_column = gender_table_matrix.loc[:,f'{gender}']
        gender_table = pd.concat([gender_table, current_column], axis=1)
        print('*')

    #gender_table = gender_table.drop(gender_table.columns[1:3], axis=1)
    gender_table['shark_name'] = ['Barbara Corcoran', 'Mark Cuban', 'Lori Greiner', 'Robert Herjavec', 'Daymond John', "Kevin O'Leary"]
    dfi.export(gender_table, 'gender_table.png')
    print('*')




    # Sample data
    categories = ['Barbara Corcoran', 'Mark Cuban', 'Lori Greiner', 'Robert Herjavec', 'Daymond John', "Kevin O'Leary"]
    values1 = list(gender_table.loc[:,'Female'])  #[10, 20, 15,8, 17, 25]
    values2 = list(gender_table.loc[:,'Male'])
    values3 = list(gender_table.loc[:,'Mixed Team'])


    # Set the positions of the bars on the y-axis
    y_pos = np.arange(len(categories))

    # Set the width of the bars
    width = 0.3  # Adjust the width as desired

    plt.style.use('seaborn')  # This line is responsible for the gray background
    # Create the figure and axes
    fig, ax = plt.subplots()

    # Plotting the first set of bars
    ax.barh(y_pos - width/2, values1, height=width, color='blue', label='Series 1')

    # Plotting the second set of bars
    ax.barh(y_pos +width/2, values2, height=width, color='lightskyblue', label='Series 2')

    # Plotting the third set of bars
    ax.barh(y_pos +3*width/2, values3, height=width, color='steelblue', label='Series 3')

    # Set the y-axis labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories)

    # Set the x-axis label
    ax.set_xlabel('Values')

    # Set the title
    ax.set_title('Amount of investment made by each shark over 3 groups')


    # Display the plot
    plt.show()
