import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
# ******************************************************************************************************************
# Function  name: convert_to_number - helper function
# input:
# return value:
# ******************************************************************************************************************

def convert_to_number(text_row, symbol_to_replace):
    if text_row is np.nan:
        return 0

    value_cap = text_row.replace(symbol_to_replace, '').replace(',', '')

    return value_cap

# ******************************************************************************************************************
# Function  name: convert_percentage_number - helper function
# input:
# return value:
# ******************************************************************************************************************
def convert_percentage_number(text_row):
    if text_row is np.nan:
        return 0

    percentage_number = float(text_row.replace('%', ''))

    return percentage_number



# ******************************************************************************************************************
# Function  name: generate_table_for_deal_equity
# input:
# return value:
# ******************************************************************************************************************
def generate_table_for_deal_equity(df_input):
    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    all_the_deals_closed = all_the_deals_closed.replace(np.nan, '', regex=True)

    # Handle missing values and strange symbols and finaly converting to int
    all_the_deals_closed['DEAL_Equity'] = all_the_deals_closed['DEAL_Equity'].apply(lambda x: convert_to_number(x, symbol_to_replace='%'))
    all_the_deals_closed = all_the_deals_closed.loc[all_the_deals_closed['DEAL_Equity'] != '', :]
    all_the_deals_closed['DEAL_Equity'] = all_the_deals_closed['DEAL_Equity'].astype('float').astype('int')


    investors_matrix = all_the_deals_closed.loc[:, 'Barbara\nCorcoran':'Guest']
    investors_matrix = investors_matrix.replace('', 0)
    investors_matrix = investors_matrix.astype('int')

    res_new_equity = np.multiply(investors_matrix.T,
                                 all_the_deals_closed['DEAL_Equity'])
    res_new_equity = res_new_equity.T
    res_new_equity['Gender'] = all_the_deals_closed['Entrepreneur Gender']

    res_new_equity_after_filter = res_new_equity.loc[res_new_equity['Gender'].isin(['Female', 'Male'])]
    list_names_sharks = ['Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary", 'Guest']

    final_table_equity = pd.DataFrame()

    grouping_by_gender = res_new_equity_after_filter.groupby('Gender')

    for gender_entrepreneur, mini_df_gender_entrepreneur in grouping_by_gender:
        print(gender_entrepreneur)
        print(mini_df_gender_entrepreneur)
        mini_df_gender_entrepreneur = mini_df_gender_entrepreneur.loc[:, 'Barbara\nCorcoran':'Guest']

        for shark_name in list_names_sharks:
            avg_equity = mini_df_gender_entrepreneur.loc[mini_df_gender_entrepreneur[shark_name] != 0, shark_name].mean()
            final_table_equity.loc[shark_name, f'{gender_entrepreneur} Avg equity'] = float(avg_equity)
            final_table_equity.loc[shark_name, f'{gender_entrepreneur} Avg equity'] = f"{final_table_equity.loc[shark_name, f'{gender_entrepreneur} Avg equity']/100:.1%}"

    print(final_table_equity)
    return final_table_equity

# ******************************************************************************************************************
# Function  name: creating_the_equity_subplot - creating the chart
# input:
# return value:
# ******************************************************************************************************************

def creating_the_equity_subplot(gender_equity_table):
    plt.style.use('seaborn')  # This line is responsible for the gray background
    # Therefore we get in ax a list of subplots of two axis
    # you can unpack it, more easier:
    fig, all_7_axis = plt.subplots(nrows=1, ncols=7, sharey=True)
    fontdict_input = {'fontsize': 16, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'White'}
    fontdict_input2 = {'fontsize': 13, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'Gray'}
    for axis, shark_name in zip(all_7_axis, list(gender_equity_table.index)):
        female_val = gender_equity_table.loc[shark_name, 'Female Avg equity']
        male_val = gender_equity_table.loc[shark_name, 'Male Avg equity']
        axis.bar(1, female_val, width=2, label='RMSE', color='lightblue')
        axis.bar(3, male_val, width=2, label='MAE')

        # Text for each bar either 'Male' or 'Female':
        axis.text(x=1, y=0.5, s='F', ha='left', va='bottom', fontdict=fontdict_input)
        axis.text(x=3, y=0.5, s='M', ha='left', va='bottom', fontdict=fontdict_input)

        # above each bar the height of each bar:
        axis.text(x=0.75, y=female_val, s=female_val, ha='left', va='bottom', fontdict=fontdict_input2,)
        axis.text(x=2.75, y=male_val, s=male_val, ha='left', va='bottom', fontdict=fontdict_input2)

        axis.set_title(shark_name,fontsize=14, weight='bold',loc='center')
        #axis.invert_yaxis() ( blood up to down )

        axis.set_xticks([])
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    df = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx", sheet_name='Sheet1')

    res=generate_table_for_deal_equity(df_input=df)
    creating_the_equity_subplot(res)
    print('*')