import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def counting_the_number_of_investments_grouped_by_gender_for_each_shark(df):

    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    all_the_deals_closed = all_the_deals_closed.replace(np.nan, '', regex=True)
    all_the_deals_closed = all_the_deals_closed.loc[all_the_deals_closed['Entrepreneur Gender'].isin(['Male', 'Female'])]

    print('*')
    sharks_name_list = ['Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn',"Kevin\nO'Leary", 'Guest']
    groups_by_gender = all_the_deals_closed.groupby('Entrepreneur Gender')
    for gender, mini_df_gender in groups_by_gender:
        print("The gender is: ", gender)
        print(mini_df_gender)
        mini_df_gender.reset_index(inplace=True, drop=True)
        gender_table_matrix = mini_df_gender.loc[:, 'Barbara\nCorcoran':'Guest']
        gender_table_matrix = gender_table_matrix.replace('', 0)
        gender_table_matrix = gender_table_matrix.astype('int')
        gender_table_matrix = gender_table_matrix.sum()
        res = gender_table_matrix.reset_index(level=0)
        res.rename(columns={res.columns[0]: 'sharks'}, inplace=True)
        res.rename(columns={res.columns[1]: f'number of investments into {gender} entrepreneur'}, inplace=True)

    return 3

if __name__ == '__main__':

    df = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx",
                       sheet_name='Sheet1')
    #df = df.fillna(' ')

    counting_the_number_of_investments_grouped_by_gender_for_each_shark(df)
    print('*')
    ##########################################################################################################################
    numpyArray = np.random.randint(20, size=(6, 2))
    # gender_column = np.array(['F', 'M', 'F', 'M', 'M', 'M'])
    # res = np.concatenate((gender_column.reshape(6, 1), numpyArray), axis=1)

    panda_df = pd.DataFrame(data=numpyArray,
                            index=["Barbara", "Mark", "Lori", "Robert", "Daymond", "Kevin"],
                            columns=["Female", "Male"])

    print(panda_df)
    plt.style.use('seaborn')  # This line is responsible for the gray background
    # Therefore we get in ax a list of subplots of two axis
    # you can unpack it, more easier:
    fig, all_6_axis = plt.subplots(nrows=1, ncols=6, sharey=True)

    fontdict_input = {'fontsize': 20, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'black'}
    fontdict_input2 = {'fontsize': 10, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'Gray'}

    for axis, shark_name in zip(all_6_axis, list(panda_df.index)):
        female_val = panda_df.loc[shark_name, 'Female']
        male_val = panda_df.loc[shark_name, 'Male']
        rects_female = axis.bar(1, female_val, width=2, label='RMSE', color='lightblue')
        rects_male = axis.bar(3, male_val, width=2, label='MAE')

        # axis.text(x=1, y=0.75, s='Solo', ha='left', va='bottom', fontsize=12, alpha=1, rotation=90, color='w',
        #           weight='bold')

        # Text for each bar either 'Male' or 'Female':
        axis.text(x=1, y=0.5, s='F', ha='left', va='bottom', fontdict=fontdict_input)
        axis.text(x=3, y=0.5, s='M', ha='left', va='bottom', fontdict=fontdict_input)

        # above each bar the height of each bar:
        axis.text(x=1, y=female_val, s=female_val, ha='left', va='bottom', fontdict=fontdict_input2)
        axis.text(x=3, y=male_val, s=male_val, ha='left', va='bottom', fontdict=fontdict_input2)

        axis.set_title(f'Shark: {shark_name}')

        axis.set_xticks([])

    plt.show()
