import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import dataframe_image as dfi


# ******************************************************************************************************************
# Function  name: counting the number of investments grouped by gender for each shark
# input:
# return value:
# ******************************************************************************************************************
def counting_the_number_of_investments_grouped_by_gender_for_each_shark(df):
    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    all_the_deals_closed = all_the_deals_closed.replace(np.nan, '', regex=True)

    # Filter for gender and group by gender
    all_the_deals_closed = all_the_deals_closed.loc[all_the_deals_closed['Entrepreneur Gender'].isin(['Male', 'Female'])]
    #column_headers = list(df.columns.values)

    # Initialize table dataframe
    gender_table = pd.DataFrame()

    # Loop through gender groups and calculating the number of investments made by each shark
    groups_by_gender = all_the_deals_closed.groupby('Entrepreneur Gender')
    for gender, mini_df_gender in groups_by_gender:
        mini_df_gender.reset_index(inplace=True, drop=True)
        gender_table_matrix = mini_df_gender.loc[:, 'Barbara\nCorcoran':'Guest']
        gender_table_matrix = gender_table_matrix.replace('', 0)
        gender_table_matrix = gender_table_matrix.astype('int')
        gender_table_matrix = gender_table_matrix.sum()

        # Here below I entered the entire input, of a specific gender, to a df column:
        gender_table[gender] = gender_table_matrix

    # Rename index (['Barbara Corcoran', 'Kevin O’Leary', 'Lori Greiner', 'Robert Herjavec', 'Mark Cuban', 'Daymond John', 'Guest'])
    gender_table.index = ['Barbara', 'Kevin', 'Lori', 'Robert', 'Mark', 'Daymond', 'Guest']
    dfi.export(gender_table, 'images/gender_table_conuter.png')
    print('*')
    return gender_table

# ******************************************************************************************************************
# Function  name: grouping_by_gender_to_create_subplots_for_each_shark(gender_table):
# input:
# return value:
# ******************************************************************************************************************


def grouping_by_gender_to_create_subplots_for_each_shark(gender_table):

    plt.style.use('seaborn')  # This line is responsible for the gray background
    # Therefore we get in ax a list of subplots of two axis
    # you can unpack it, more easier:
    fig, all_6_axis = plt.subplots(nrows=1, ncols=7, sharey=True)
    fontdict_input = {'fontsize': 16, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'White'}
    fontdict_input2 = {'fontsize': 13, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'Gray'}
    for axis, shark_name in zip(all_6_axis, list(gender_table.index)):
        female_val = gender_table.loc[shark_name, 'Female']
        male_val = gender_table.loc[shark_name, 'Male']
        axis.bar(1, female_val, width=2, label='RMSE', color='navy')
        axis.bar(3, male_val, width=2, label='MAE',color = 'cornflowerblue')


        all_6_axis[0].set_ylabel('Number of investments made by each shark', fontsize=17,
                                 fontweight='bold',fontname='Franklin Gothic Medium Cond')

        # Text for each bar either 'Male' or 'Female':
        axis.text(x=1, y=0.5, s='F', ha='left', va='bottom', fontdict=fontdict_input)
        axis.text(x=3, y=0.5, s='M', ha='left', va='bottom', fontdict=fontdict_input)

        # above each bar the height of each bar:
        axis.text(x=1, y=female_val, s=female_val, ha='left', va='bottom', fontdict=fontdict_input2)
        axis.text(x=3, y=male_val, s=male_val, ha='left', va='bottom', fontdict=fontdict_input2)

        axis.set_title(shark_name,fontsize=21, weight='bold',fontname='Franklin Gothic Medium Cond')

        axis.set_xticks([])
    plt.show()


if __name__ == '__main__':

    df = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx",sheet_name='Sheet1')

    res=counting_the_number_of_investments_grouped_by_gender_for_each_shark(df)
    grouping_by_gender_to_create_subplots_for_each_shark(res)
    print('*')
    ##########################################################################################################################

