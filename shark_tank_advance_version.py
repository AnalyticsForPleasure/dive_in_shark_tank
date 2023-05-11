import re

import numpy as np
import pandas as pd


def convert_to_number(text_row, symbol_to_replace):
    if text_row is np.nan:
        return 0

    value_cap = text_row.replace(symbol_to_replace, '').replace(',', '')

    return value_cap


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


def generate_table_for_deal_eqauty(df_input):
    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    all_the_deals_closed = all_the_deals_closed.replace(np.nan, '', regex=True)

    # Handle missing values and strange symbols and finaly converting to int
    all_the_deals_closed['DEAL_Equity'] = all_the_deals_closed['DEAL_Equity'].apply(
        lambda x: convert_to_number(x, symbol_to_replace='%'))
    all_the_deals_closed = all_the_deals_closed.loc[all_the_deals_closed['DEAL_Equity'] != '', :]
    all_the_deals_closed['DEAL_Equity'] = all_the_deals_closed['DEAL_Equity'].astype('float').astype('int')

    investors_matrix = all_the_deals_closed.iloc[:, 17:24]
    investors_matrix = investors_matrix.replace('', 0)
    investors_matrix = investors_matrix.astype('int')

    res_new_equity = np.multiply(investors_matrix.T,
                                 all_the_deals_closed['DEAL_Equity'])
    res_new_equity = res_new_equity.T
    res_new_equity['Gender'] = all_the_deals_closed['Entrepreneur Gender']
    res_new_equity_after_filter = res_new_equity.loc[res_new_equity['Gender'].isin(['Female','Male'])]
    res_new_equity_after_filter_with_out_zeros = res_new_equity_after_filter.replace(0,'' , regex=True)

    final_table_equity = pd.DataFrame()
    grouping_by_gender = res_new_equity_after_filter_with_out_zeros.groupby('Gender')
    for gender_enrepreneur, mini_df_gender_enrepreneur in grouping_by_gender:
        print(gender_enrepreneur)
        print(mini_df_gender_enrepreneur)
        mini_df_gender_enrepreneur = mini_df_gender_enrepreneur.loc[:, 'Barbara\nCorcoran':'Guest']
        avg_investment_equity_by_a_shark =  mini_df_gender_enrepreneur.mean(axis=0)
        final_table_equity[gender_enrepreneur] = avg_investment_equity_by_a_shark


    final_table_equity.index = ['Barbara', 'Kevin', 'Lori', 'Robert', 'Mark', 'Daymond', 'Guest']
    print('*')

    return final_table_equity


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


if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    df = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx",
                       sheet_name='Sheet1')

    # retriving_info_about_royalty_equity_and_loans(df_input)
    # print('*')

    generate_table_for_deal_eqauty(df_input=df)

    ##########################################################################################################################
    # In order to do the the dynamic Waffle chart :
    prepare_df_for_each_season_for_waffle_chart(df)
    print('*')
    # result = retrieving_negotiation_details(df_input)
    # print('*')
    # https://towardsdatascience.com/9-visualizations-to-show-proportions-or-percentages-instead-of-a-pie-chart-4e8d81617451
