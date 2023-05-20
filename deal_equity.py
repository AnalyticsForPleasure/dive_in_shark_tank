import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

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
    all_the_deals_closed['DEAL_Equity'] = all_the_deals_closed['DEAL_Equity'].apply(
        lambda x: convert_to_number(x, symbol_to_replace='%'))
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
    list_names_sharks = ['Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn',
                         "Kevin\nO'Leary", 'Guest']

    final_table_equity = pd.DataFrame()

    grouping_by_gender = res_new_equity_after_filter.groupby('Gender')

    for gender_entrepreneur, mini_df_gender_entrepreneur in grouping_by_gender:
        # print(gender_entrepreneur)
        # print(mini_df_gender_entrepreneur)
        mini_df_gender_entrepreneur = mini_df_gender_entrepreneur.loc[:, 'Barbara\nCorcoran':'Guest']

        for shark_name in list_names_sharks:
            avg_equity = mini_df_gender_entrepreneur.loc[
                mini_df_gender_entrepreneur[shark_name] != 0, shark_name].mean()
            final_table_equity.loc[shark_name, f'{gender_entrepreneur} Avg equity'] = float(avg_equity)
            # Don't arase this line below - this line is important for display the table result:
            # final_table_equity.loc[shark_name, f'{gender_entrepreneur} Avg equity'] = f"{final_table_equity.loc[shark_name, f'{gender_entrepreneur} Avg equity']/100:.1%}"

    # print(final_table_equity)
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
    fontdict_input = {'fontsize': 18, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'White'}
    fontdict_input2 = {'fontsize': 13, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'gray'}

    # res['Female Avg equity'] = (res['Female Avg equity']).apply(lambda r:"{:.2%}".format(r))
    for axis, shark_name in zip(all_7_axis, list(gender_equity_table.index)):
        female_val = gender_equity_table.loc[shark_name, 'Female Avg equity']
        female_val_labels = "{:.1f}".format(female_val)

        male_val = gender_equity_table.loc[shark_name, 'Male Avg equity']
        male_val_labels = "{:.1f}".format(male_val)

        axis.bar(1, female_val, width=2, label='RMSE', color='darkblue')
        axis.bar(3, male_val, width=2, label='MAE', color='dodgerblue', hatch='.O')

        # all_7_axis.set_xlabel(shark_name, fontsize=14)

        # Setting the y label for all sub plots
        all_7_axis[0].set_ylabel('The avg equity (%)', fontsize=19, fontweight='bold')
        axis.set_xticks([])
        axis.set_xlabel(shark_name,fontweight='bold',fontsize=15 )
        # Text for each bar either 'Male' or 'Female':
        axis.text(x=1, y=0.15, s='F', ha='left', va='bottom', fontdict=fontdict_input)
        axis.text(x=3, y=0.15, s='M', ha='left', va='bottom', fontdict=fontdict_input)

        # above each bar the height of each bar:
        axis.text(x=0.75, y=female_val, s=female_val_labels, ha='left', va='bottom', fontdict=fontdict_input2, )
        axis.text(x=2.75, y=male_val, s=male_val_labels, ha='left', va='bottom', fontdict=fontdict_input2)

    plt.suptitle('The average equity invested by each shark in entrepreneurs, broken down by gender', y=0.93,
                 fontsize=25, fontweight='heavy',fontname='Franklin Gothic Medium Cond')

    #plt.savefig('deal_equity.jpg', dpi=250, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    pd.set_option('display.max_rows', 1000)
    # first method
    plt.rcParams['font.family']='instrument'
    # matplotlib.rcParams['font.family'] = ['instrument serif']
    # plt.rcParams['Instrument Serif'] = ['Instrument Serif']
    # print(plt.rcParams)
    # exit(555)

    df = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx",
                       sheet_name='Sheet1')

    plt.style.use('seaborn')
    res = generate_table_for_deal_equity(df)#(df_input=d f)
    creating_the_equity_subplot(res)
    print('*')
