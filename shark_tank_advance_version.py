import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ******************************************************************************************************************
# Function  name: convert_to_number - Helper function
# input:
# return value:
# ******************************************************************************************************************
def convert_to_number(text_row, symbol_to_replace):
    if text_row is np.nan:
        return 0

    value_cap = text_row.replace(symbol_to_replace, '').replace(',', '')

    return value_cap

# ******************************************************************************************************************
# Function  name: convert_percentage_number - Helper function
# input:
# return value:
# ******************************************************************************************************************
def convert_percentage_number(text_row):
    if text_row is np.nan:
        return 0

    percentage_number = float(text_row.replace('%', ''))

    return percentage_number


# ******************************************************************************************************************
# Function  name: retrieving_negotiation_details
# input:
# return value:
# ******************************************************************************************************************
def retrieving_negotiation_details(df):
    df_deals_closed = df.loc[:, ['ASK', 'DEAL']].dropna()  # selecting only 6 relevant columns
    # Working on the valuation part:
    df_deals_closed['ASK', 'Valuation_ASK'] = df_deals_closed.loc[:, ('ASK', 'Valuation')].apply(
        lambda x: convert_to_number(x))
    df_deals_closed['DEAL', 'Valuation_DEAL'] = df_deals_closed.loc[:, ('DEAL', 'Valuation')].apply(
        lambda x: convert_to_number(x))
    # Working on the equity part:
    df_deals_closed['ASK', 'Equity_ASK'] = df_deals_closed.loc[:, ('ASK', 'Equity')].apply(
        lambda x: convert_percentage_number(x))
    df_deals_closed['DEAL', 'Equity_DEAL'] = df_deals_closed.loc[:, ('DEAL', 'Equity')].apply(
        lambda x: convert_percentage_number(x))
    df_deals_closed['final_result', 'ratio_Deal_VS_ASK_Valuation'] = df_deals_closed['DEAL', 'Valuation_DEAL'] / \
                                                                     df_deals_closed['ASK', 'Valuation_ASK']
    print('*')
    # let's now convert continuous data to categorical Data -
    df_deals_closed['willing_to_invest'] = pd.cut(df_deals_closed['final_result', 'ratio_Deal_VS_ASK_Valuation'],
                                                  bins=[0.2, 1, 1.5, 2],
                                                  labels=['Lowly_desire', 'desire', 'Highly_desire '])
    res = df_deals_closed['willing_to_invest'].value_counts()
    res = res.reset_index(level=0)
    res.rename(columns={res.columns[0]: 'measurement'}, inplace=True)
    res.rename(columns={res.columns[1]: 'counter_measurement'}, inplace=True)
    tatal_value = res['counter_measurement'].sum()
    pos = 1
    for pos in range(len(res)):
        res['percentage_measurement'] = res.loc[pos, 'counter_measurement'] / tatal_value
        pos += pos
    # res['percentage_measurement'] = (res['percentage_measurement']).apply(lambda r:"{:.2%}".format(r))
    res['Y'] = [1] * len(res)
    list_x = list(range(0, len(res)))
    res['X'] = list_x

    print('*')

    return res


# ******************************************************************************************************************
# Function  name: retriving_info_about_royalty_equity_and_loans
# input:
# return value:
# ******************************************************************************************************************
def retriving_info_about_royalty_equity_and_loans(df):
    df.sort_values('Details / Notes', inplace=True)
    dict_royalties_loans_equities = {'royalty': 0, 'loan': 0, 'equity': 0}
    for k in dict_royalties_loans_equities.keys():
        if k is not 'equity':
            df[f'contains_{k}'] = df.loc[:, 'Details / Notes'].str.contains(k, case=False)
        else:
            df[f'contains_{k}'] = df.loc[:, 'Details / Notes'].str.contains('equity|perpetual', regex=True,
                                                                            flags=re.IGNORECASE)

        dict_royalties_loans_equities[k] = np.sum(df[f'contains_{k}'])  # {'royalty': 22, 'loan': 15, 'equity': 16}
    print('*')
    return dict_royalties_loans_equities


# ******************************************************************************************************************
# Function  name: prepare_df_for_each_season_for_waffle_chart
# input:
# return value:
# ******************************************************************************************************************

def prepare_df_for_each_season_for_waffle_chart(df_input):
    all_the_deals_closed = df_input.loc[df_input['Deal'] == 'Yes', :]
    all_the_deals_closed = all_the_deals_closed.replace(np.nan, '', regex=True)
    print('*')
    all_the_deals_closed['DEAL_Amount'] = all_the_deals_closed['DEAL_Amount'].apply(
        lambda x: convert_to_number(x, symbol_to_replace='$'))
    all_the_deals_closed = all_the_deals_closed.loc[all_the_deals_closed['DEAL_Amount'] != '', :]
    all_the_deals_closed['DEAL_Amount'] = all_the_deals_closed['DEAL_Amount'].astype('int')
    column_headers = list(all_the_deals_closed.columns.values)
    groups_by_season = all_the_deals_closed.groupby('Season')
    for season_number, mini_df_season_number in groups_by_season:
        # print(f'Season #{season_number}')
        mini_df_season_number.reset_index(inplace=True, drop=True)
        investors_matrix = mini_df_season_number.iloc[:, 17:24]
        investors_matrix = investors_matrix.replace('', 0)
        investors_matrix = investors_matrix.astype('int')
        mini_df_season_number['number_of_investors'] = investors_matrix.sum(axis=1)
        mini_df_season_number['investment_per_investor'] = mini_df_season_number['DEAL_Amount'] / \
                                                           mini_df_season_number['number_of_investors']

        infinite_investment = mini_df_season_number['investment_per_investor'] == np.inf
        mini_df_season_number.loc[infinite_investment, 'investment_per_investor'] = 0
        res = np.multiply(investors_matrix.T,
                          mini_df_season_number['investment_per_investor'])

        res2 = res.sum(axis=1)
        print(f'Season #{season_number}:\n {res2}')
        print('*' * 50)



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
        axis.bar(1, female_val, width=2, label='RMSE', color='lightblue')
        axis.bar(3, male_val, width=2, label='MAE')

        # Text for each bar either 'Male' or 'Female':
        axis.text(x=1, y=0.5, s='F', ha='left', va='bottom', fontdict=fontdict_input)
        axis.text(x=3, y=0.5, s='M', ha='left', va='bottom', fontdict=fontdict_input)

        # above each bar the height of each bar:
        axis.text(x=1, y=female_val, s=female_val, ha='left', va='bottom', fontdict=fontdict_input2)
        axis.text(x=3, y=male_val, s=male_val, ha='left', va='bottom', fontdict=fontdict_input2)

        axis.set_title(shark_name,fontsize=14, weight='bold')

        axis.set_xticks([])
    plt.show()



if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    df = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx",
                       sheet_name='Sheet1')

    # retriving_info_about_royalty_equity_and_loans(df_input)
    # print('*')


    print('*')
    ##########################################################################################################################
    # In order to do the the dynamic Waffle chart :
    prepare_df_for_each_season_for_waffle_chart(df)
    print('*')
    # result = retrieving_negotiation_details(df_input)
    # print('*')
    # https://towardsdatascience.com/9-visualizations-to-show-proportions-or-percentages-instead-of-a-pie-chart-4e8d81617451
