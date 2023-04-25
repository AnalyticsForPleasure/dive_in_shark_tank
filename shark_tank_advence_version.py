import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import dataframe_image as dfi  # Should install: "dataframe-image"
import seaborn as sns
#import plotly.express as px
import re


def convert_to_number(text_row):
    if text_row is np.nan:
        return 0

    value_cap = int(text_row.replace('$', '').replace(',', ''))

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
    res
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

        dict_royalties_loans_equities[k] = np.sum(df[f'contains_{k}']) # {'royalty': 22, 'loan': 15, 'equity': 16}
    print('*')
    return dict_royalties_loans_equities

if __name__ == '__main__':
    pd.set_option('display.max_rows', 500)
    df = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx", sheet_name='Sheet1')  # header=[0, 1]


    #retriving_info_about_royalty_equity_and_loans(df)
    #print('*')


    # # create a sample dataframe
    # df = pd.DataFrame({'text': ['I love pandas', 'Pandas are awesome', 'Python is great']})
    #
    # # search for the word 'pandas' in the 'text' column
    # df['contains_pandas'] = df['text'].str.contains('pandas', case=False)

    result = retrieving_negotiation_details(df)
    print('*')

    # https://towardsdatascience.com/9-visualizations-to-show-proportions-or-percentages-instead-of-a-pie-chart-4e8d81617451

    # check the column 'willing_to_invest' it over the seasons
    # ratio_ask_to_deal_valiation
    print('*')
    #
    # pal_ = list(sns.color_palette(palette='plasma_r',
    #                               n_colors=len(res.measurement)).as_hex())
    # # create a laebls list for each bubble
    # label = [i + '<br>' + str(j) + '<br>' + str(k) + '%' for i, j, k in zip(res.measurement,
    #                                                                         res.counter_measurement,
    #                                                                         res.percentage_measurement)]
    # #
    # fig = px.scatter(res, x='X', y='Y',
    #                  color='measurement',
    #                  color_discrete_sequence=pal_,
    #                  size='counter_measurement',
    #                  text=label,
    #                  size_max=90)
    # fig.update_layout(width=900,
    #                   height=320,
    #                   margin=dict(t=50, l=0, r=0, b=0),
    #                   showlegend=False)
    # fig.update_traces(textposition='top center')
    # fig.update_xaxes(showgrid=False, zeroline=False, visible=False)
    # fig.update_yaxes(showgrid=False, zeroline=False, visible=False)
    # fig.update_layout({'plot_bgcolor': 'white',
    #                    'paper_bgcolor': 'white'})
    # fig.show()
    #
    # print('*')
