import pandas as pd
import dataframe_image as dfi
import numpy as np

from shark_tank_charts import getting_top_5_investments_made_by_a_shark_over_stack_bar_chart
from shark_tank_charts import pie_chart_which_illustrate_the_number_of_investments_each_season_over_the_years

from shark_tank_charts import two_bar_plot_shows_multiple_entrepreneurs_VS_individual_entrepreneur
from shark_tank_charts import creating_bidirectional_bar_chart_by_categories
from shark_tank_charts import slope_chart_for_industries_have_gotten_hotter_or_colder_over_6_seasons


# **************************************************************************************************************
# Function  name: helper function for Define a function to count the number of elements in a list
# input:
# return value:
# ***************************************************************************************************************

def count_elements_in_list(lst):
    return float(len(lst))


# **************************************************************************************************************
# Function  name: helper function for "get_categories_each_shark_invested_his_money" function
# input:
# return value:
# ****************************************************************************************************************

def get_top_n(final_table, n=1):
    return df.nlargest(n, 'amount_of_investments')


# **************************************************************************************************************
# Function  name: get_categories_each_shark_invested_his_money
# input:
# return value: For each shark the amount of money he invested in the entrepreneur by categories
# ****************************************************************************************************************
def get_categories_each_shark_invested_his_money(all_the_deals_closed_over_the_years):
    df_starting = pd.DataFrame({'shark_name': [],
                                'category': [],
                                'number_of_investments_per_category': [],
                                'amount_of_investments_per_category': []
                                })

    shark_name_list = []
    category_list = []
    investments_per_category_made_by_specific_shark_list = []
    sum_investments_per_category_made_by_specific_shark_list = []

    grouping_by_shark_names = all_the_deals_closed_over_the_years.groupby('chosen_shark')

    for shark_name, mini_df_shark_name in grouping_by_shark_names:
        # print(shark_name)
        # print(mini_df_shark_name)
        mini_df_shark_name['askedfor'].sum()
        print('*')
        grouping_category_by_shark = mini_df_shark_name.groupby('category')
        for category_by_shark, mini_df_category_by_shark in grouping_category_by_shark:
            # print(category_by_shark)
            # print(mini_df_category_by_shark)
            number_of_investments_per_category_made_by_specific_shark = mini_df_category_by_shark['askedfor'].shape[0]
            total_investments_per_category_made_by_specific_shark = mini_df_category_by_shark['askedfor'].sum()
            # res = mini_df_category_by_shark['askedfor'].sum()
            print('*')

            shark_name_list.append(shark_name)
            category_list.append(category_by_shark)
            investments_per_category_made_by_specific_shark_list.append(
                number_of_investments_per_category_made_by_specific_shark)
            sum_investments_per_category_made_by_specific_shark_list.append(
                total_investments_per_category_made_by_specific_shark)
        print('*')

    df_starting = {'shark_name': shark_name_list,
                   'Category_selected': category_list,
                   'Number of investments made': investments_per_category_made_by_specific_shark_list,
                   'Sum of money investments made': sum_investments_per_category_made_by_specific_shark_list
                   }
    print('*')

    final_table = pd.DataFrame(df_starting,
                               columns=['shark_name', 'Category_selected', 'Number of investments made',
                                        'Sum of money investments made'])

    final_table.sort_values(by=['shark_name', 'Sum of money investments made'], ascending=[True, False], inplace=True)

    # Getting for each shark the top 5 investments made :
    res = final_table.groupby('shark_name')
    # top_investment_of_a_shark = (final_table.groupby('shark_name')['Sum of money investments made']
    #                              .apply(lambda ser: ser.drop_duplicates().nlargest(5))
    #                              # .droplevel(level=1)
    #                              .sort_index()
    #                              .reset_index()
    #                              )

    top_investment_of_a_shark = final_table.groupby('shark_name').apply(lambda mini_df: mini_df.iloc[:5, :])
    top_investment_of_a_shark.index = np.arange(0, top_investment_of_a_shark.shape[0])
    # Here I used the pivot table function
    metrics_df = pd.pivot_table(top_investment_of_a_shark, values='Sum of money investments made', index='shark_name',
                                columns='Category_selected')
    metrics_df.reset_index(inplace=True)
    metrics_df.fillna(0, inplace=True)
    # my_metrics_df = metrics_df.iloc[:,[0,7,15,22,23,24]] # Electronics(7),Novelties(15),Specialty_Food(22),Storage_and_Cleaning_Products(23),Toys_and_Games(24)
    print('*')
    return metrics_df


# **************************************************************************************************************
# Function  name: getting_avg_valuation_of_each_shark_willing_to_invest_each_season
# input:
# return value: avg valuation of each shark willing to investeach season
# ****************************************************************************************************************
def getting_avg_valuation_of_each_shark_willing_to_invest_each_season(all_the_deals_closed_over_the_years):
    df_starting = pd.DataFrame({'shark_name': [],
                                'season_number': [],
                                'avg_valuation_per_season_show': [],
                                'tatal_valuation_per_season_show': []
                                })

    shark_name_list = []
    list_of_seasons = []
    avg_valuation_per_season_show_list = []
    tatal_valuation_per_season_show_list = []

    grouping_by_shark_name = all_the_deals_closed_over_the_years.groupby('chosen_shark')
    for shark_name, min_df_shark in grouping_by_shark_name:
        # print(shark_name)
        # print(min_df_shark)
        number_of_investments_made = min_df_shark.shape[0]
        grouping_by_number_of_investments_made_per_season = min_df_shark.groupby('season')
        for season, valuation_df_by_season in grouping_by_number_of_investments_made_per_season:
            # print(season)
            # print(valuation_df_by_season)
            avg_valuation_per_season_show = valuation_df_by_season['valuation'].mean()
            tatal_valuation_per_season_show = valuation_df_by_season['valuation'].sum()
            print('*')

            shark_name_list.append(shark_name)
            list_of_seasons.append(season)
            avg_valuation_per_season_show_list.append(avg_valuation_per_season_show)
            tatal_valuation_per_season_show_list.append(tatal_valuation_per_season_show)

        print('*')

        df_starting = {'shark_name': shark_name_list,
                       'season_number': list_of_seasons,
                       'avg_valuation_per_season_show': avg_valuation_per_season_show_list,
                       'sum_valuation_per_season_show': tatal_valuation_per_season_show_list}

    final_table = pd.DataFrame(df_starting,
                               columns=['shark_name', 'season_number', 'avg_valuation_per_season_show',
                                        'sum_valuation_per_season_show'])
    print('*')

    return final_table


# **************************************************************************************************************
# Function  name: getting_the_shark_name_investing_in_multiple_entrepreneurs_in_dif_fields
# input:
# return value: information about each shark investments upon multiple entrepreneurs and the fields they invested
# ****************************************************************************************************************
def getting_the_shark_name_investing_in_multiple_entrepreneurs_in_dif_fields(all_the_deals_closed_over_the_years):
    deals_closed_for_multiple_entrepreneurs = all_the_deals_closed_over_the_years.loc[
        (all_the_deals_closed_over_the_years['multiple_entreprenuers'] == True)]
    grouping_by_shark_name = deals_closed_for_multiple_entrepreneurs.groupby('chosen_shark')
    for shark_name, mini_df_shark in grouping_by_shark_name:
        # print(shark_name)
        # print(mini_df_shark)
        res = mini_df_shark['category'].value_counts()
        print('*')

    return res


# **************************************************************************************************************
# Function  name: finding_the_shark_which_known_as_willing_to_takes_risky_investment
# input:
# return value: information about each shark investments upon multiple entrepreneurs and the fields they invested
# ****************************************************************************************************************
def finding_the_shark_which_known_as_willing_to_takes_risky_investment(closed_deals):
    # first constraint : dict_sharks which invest in risky categories fields
    res = closed_deals['category'].value_counts()
    K = 10  # number of less popular categories for investing
    final_res = res.tail(K)
    categories_which_known_as_risky_investment = list(final_res.index.values)
    filtered_df_by_risky_categories = closed_deals[
        closed_deals['category'].isin(categories_which_known_as_risky_investment)]
    print('*')
    # second constraint : Sharks which invest a lot of money
    upper_bound_ask = 200000  # ( Two hundreds dollars)
    filter_by_money_investment = filtered_df_by_risky_categories.loc[
                                 filtered_df_by_risky_categories['askedfor'] > upper_bound_ask, :]
    number_of_results_filter_by_money_investment = filter_by_money_investment.shape[0]

    # OR
    print('*')
    # second constraint : OR Sharks who took exchange for stake more than 25%
    lowest_bound_presantage = 25
    filter_by_exchange_for_stake = filtered_df_by_risky_categories.loc[
                                   filtered_df_by_risky_categories['exchangeforstake'] > lowest_bound_presantage, :]
    print('*')
    number_of_results_filter_by_exchange_for_stake = filter_by_exchange_for_stake.shape[0]
    print('*')
    if (number_of_results_filter_by_money_investment > number_of_results_filter_by_exchange_for_stake):
        result_df = filter_by_money_investment
    else:
        result_df = filter_by_exchange_for_stake

    print('*')

    return result_df


# **************************************************************************************************************
# Function  name: get_number_of_investments_each_season_over_the_years
# input:
# return value:
# ****************************************************************************************************************
def get_number_of_investments_each_season_over_the_years(all_the_deals_closed):
    res = all_the_deals_closed['season'].value_counts().to_frame()
    res = res.reset_index(level=0)
    res.rename(columns={res.columns[0]: 'season_number'}, inplace=True)
    res.rename(columns={res.columns[1]: 'amount_of_investments_over_each_season'}, inplace=True)
    res['season_number'] = res['season_number'].astype(str) + ' season'  # adding a string into specific column
    print('*')

    return res


# **************************************************************************************************************
# Function  name: ratio_of_investments_of_each_shark_choose_between_multiple_entrepreneurs_VS_individual_entrepreneur
# input:
# return value:
# ****************************************************************************************************************
def ratio_of_investments_of_each_shark_choose_between_multiple_entrepreneurs_VS_individual_entrepreneur(
        all_the_deals_closed):
    mapping = {True: 'individual entrepreneur',
               False: 'multiple entrepreneurs'}

    all_the_deals_closed['kind_of_entrepreneurs'] = all_the_deals_closed['multiple_entreprenuers'].apply(
        lambda x: mapping[x])
    filter_data_individual = all_the_deals_closed.loc[
                             all_the_deals_closed['kind_of_entrepreneurs'] == 'individual entrepreneur', :]
    individual_entrepreneur = filter_data_individual['chosen_shark'].value_counts()
    individual_entrepreneur_df = individual_entrepreneur.reset_index()
    individual_entrepreneur_df.rename(
        columns={individual_entrepreneur_df.columns[1]: 'counter_of_individual_entrepreneur'}, inplace=True)
    individual_entrepreneur_df.rename(columns={individual_entrepreneur_df.columns[0]: 'chosen_shark'}, inplace=True)
    print('*')

    filter_data_multiple = all_the_deals_closed.loc[
                           all_the_deals_closed['kind_of_entrepreneurs'] == 'multiple entrepreneurs', :]
    multiple_entrepreneur = filter_data_multiple['chosen_shark'].value_counts()
    multiple_entrepreneur_df = multiple_entrepreneur.reset_index()
    multiple_entrepreneur_df.rename(columns={multiple_entrepreneur_df.columns[1]: 'counter_of_multiple_entrepreneur'},
                                    inplace=True)
    multiple_entrepreneur_df.rename(columns={multiple_entrepreneur_df.columns[0]: 'chosen_shark'}, inplace=True)
    print('*')

    return individual_entrepreneur_df, multiple_entrepreneur_df


# **************************************************************************************************************
# Function  name: retrieving_the_amount_of_investments_and_non_investments_by_categories
# input:
# return value:
# ****************************************************************************************************************
def retrieving_the_amount_of_investments_and_non_investments_by_categories(df):
    closed_deals = df.loc[df['deal'] == True, :]
    close_deals_by_category = closed_deals['category'].value_counts().head(n=14)
    close_deals_by_category = close_deals_by_category.reset_index(level=0)
    close_deals_by_category.rename(columns={close_deals_by_category.columns[0]: 'selected_categories'}, inplace=True)
    close_deals_by_category.rename(columns={close_deals_by_category.columns[1]: 'counter_closed_deals'}, inplace=True)
    list_of_unclose_deals_categories = list(close_deals_by_category['selected_categories'])
    print('*')
    unclosed_deals = df.loc[df['deal'] == False, :]
    filtered_unclosed_deals = unclosed_deals[unclosed_deals['category'].isin(list_of_unclose_deals_categories)]
    unclose_deals_by_category = filtered_unclosed_deals['category'].value_counts()
    unclose_deals_by_category = unclose_deals_by_category.reset_index(level=0)
    unclose_deals_by_category.rename(columns={unclose_deals_by_category.columns[0]: 'selected_categories'},
                                     inplace=True)
    unclose_deals_by_category.rename(columns={unclose_deals_by_category.columns[1]: 'counter_unclosed_deals'},
                                     inplace=True)

    close_deals_by_category['counter_unclosed_deals'] = unclose_deals_by_category['counter_unclosed_deals']
    summary_table = close_deals_by_category
    print('*')

    return summary_table


# **************************************************************************************************************
# Function  name: which_industries_have_gotten_hotter_or_colder_over_6_seasons
# input:
# return value:
# ****************************************************************************************************************
def which_industries_have_gotten_hotter_or_colder_over_6_seasons(df):
    closed_deals_first_season = df.loc[(df['deal'] == True) & (df['season'] == 1)]  # 27 closed deals in season 1
    counter_1_season = closed_deals_first_season['category'].value_counts()
    counter_1_season = counter_1_season.drop(
        ['Fitness Equipment'])  # dropping one category in order to compare to season 6
    counter_1_season = counter_1_season.reset_index(level=0)
    counter_1_season.rename(columns={counter_1_season.columns[0]: 'categories'}, inplace=True)
    counter_1_season.rename(columns={counter_1_season.columns[1]: 'counter_categories_season_1'}, inplace=True)
    counter_1_season.sort_values(by='categories', inplace=True, ascending=False)
    avg_valuation_1_season = closed_deals_first_season.groupby(['category'])['valuation'].mean()

    categories_in_season_1 = list(counter_1_season.loc[:, 'categories'])
    closed_deals_sixth_season = df.loc[(df['deal'] == True) & (df['season'] == 6)]
    closed_deals_sixth_season = closed_deals_sixth_season.loc[
        closed_deals_sixth_season['category'].isin(categories_in_season_1)]
    counter_6_season = closed_deals_sixth_season['category'].value_counts()
    counter_6_season = counter_6_season.reset_index(level=0)
    counter_6_season.rename(columns={counter_6_season.columns[0]: 'categories'}, inplace=True)
    counter_6_season.rename(columns={counter_6_season.columns[1]: 'counter_categories_season_6'}, inplace=True)

    counter_6_season.sort_values(by='categories', inplace=True, ascending=False)
    avg_valuation_6_season = closed_deals_sixth_season.groupby(['category'])['valuation'].mean()

    # Lets nerge the two data together:
    final_res = counter_1_season.merge(counter_6_season, on='categories', how='inner')
    print('*')
    # TODO : continue with the for + if statement
    #
    # my_result =[]
    # for category_row in final_res.index :
    #
    #
    #     category_row = 1
    #     current_row = final_res.loc[[category_row],:]
    #     if final_res.loc[category_row,'counter_categories_season_1'] == final_res.loc[category_row,'counter_categories_season_6']:
    #         final_res.drop(category_row)
    #     else:
    #         final_res.append(current_row)
    #         print('*')
    #
    #         category_row += category_row
    final_table_result = final_res.loc[[0, 5, 6, 8, 11], :]
    print('*')
    return final_table_result


# **************************************************************************************************************
# Function  name: counting_the_number_of_entrepreneuers_in_a_group_for_pitching
# input:
# return value:
# ****************************************************************************************************************
def counting_the_number_of_entrepreneuers_in_a_group_for_pitching(df):
    df = df.dropna(subset=['entrepreneurs'])
    # counting the number of entrepreneurs we have:
    df['entrepreneurs_output'] = df['entrepreneurs'].str.split(',|&| and ')
    # Apply the function to each row in the column
    df['entrepreneurs_output'] = df['entrepreneurs_output'].apply(count_elements_in_list)
    df['entrepreneurs_output'] = df['entrepreneurs_output'].apply(lambda x: int(x))
    # number of entrepreneurs in the group how gave a pitch:
    final_result = df['entrepreneurs_output'].value_counts().reset_index(level=0)
    print(df)
    return final_result


if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    df = pd.read_csv('../data/shark_tank_companies.csv')
    print('*')
    # short info about the data:
    print(df.columns.values)  # list of column names
    print(df.shape[0])  # 495 rows
    print(df.shape[1])  # 19 columns
    print('*')

    # Adding a column which shows us how is the choosen shark selected
    all_the_deals_closed = df.loc[df['deal'] == True, :]
    all_the_deals_closed['Shark_which_invested'] = np.random.randint(1, 11, size=251)
    print('*')

    column_headers = list(df.columns.values)
    print('*')

    # instead of writing the entire sharked  hard coded, we will write the coded this way:
    shark_columns = [f'shark{i}' for i in range(1, 6)]
    shark_names = np.unique(df[shark_columns])
    dict_sharks = dict(zip(range(len(shark_names)), shark_names))

    all_the_deals_closed['chosen_shark'] = all_the_deals_closed['Shark_which_invested'].map(dict_sharks)

    # 1.What is the name of the shark who appeared the most seasons?

    # 2.How many deals have been closed over the years?

    # deals_closed = df['deal'].value_counts()  # True: 251 , False: 244
    # print(f'The amount of closed deals / rejected deals over the entire seasons:{deals_closed}')
    #
    # deals_closed_precentage = df['deal'].value_counts(normalize=True)

    # 3. How many deals have been closed & rejected over each season?
    #     res =df.groupby('season')['deal'].value_counts().to_frame()
    #     print(f'The number of closed deal & deal which were rejected over each seasons are:{res}')
    #
    #     # This is not working
    #     dfi.export(res, 'res_image1.png')
    #     print('*')

    # 4. What is the name of the shark who appeared in the most episodes? How many?

    #  what is the number of investments in each season?
    # res = get_number_of_investments_each_season_over_the_years(all_the_deals_closed)
    # pie_chart_which_illustrate_the_number_of_investments_each_season_over_the_years(res)
    print('*')

    # 16. In which city each shark willing invests his money? How much money each shark invested in a different location?
    # all_the_deals_closed = df.loc[df['deal'] == True,:]
    # location_of_all_deals_closed = all_the_deals_closed['location'].value_counts()  # 19 closing deals were closed in L.A location
    # print(f'The deals were closed over the states at:{location_of_all_deals_closed}')
    #
    # all_the_deals_closed = df.loc[df['deal'] == True,:]
    # all_the_deals_closed['Shark_which_invested'] = np.random.randint(1,11, size=251)
    # print('*')
    #
    # #instead of writing the entire sharked  hard coded, we will write the coded this way:
    # shark_columns = [f'shark{i}' for i in range(1, 6)]
    # shark_names = np.unique(df[shark_columns])
    # dict_sharks = dict(zip(range(len(shark_names)), shark_names))
    #
    # all_the_deals_closed['chosen_shark'] = all_the_deals_closed['Shark_which_invested'].map(dict_sharks)
    # print('*')

    # 6. How many categories do we have? ( The dict_sharks invested in diffrent 51 categories )
    # all_categories = pd.unique(all_the_deals_closed['category'])
    # all_the_deals_closed['category'].value_counts() # We can see the shark made the most investment over the 'Specialty food' category.
    # print('*')

    # In which category each shark invested his money?
    # res = get_categories_each_shark_invested_his_money(all_the_deals_closed)
    # getting_top_5_investments_made_by_a_shark_over_stack_bar_chart(res)
    # print('*')
    # The amount of money the dict_sharks invested in multiple_entreprenuers
    # closed_deals = df.loc[df['deal'] == True,:] # first condition
    # closed_deals_invested_in_multiple_entreprenuers = closed_deals.loc[closed_deals['multiple_entreprenuers']==True,:]  # Second condition
    # print(f'Number of deals for multiple entreprenuers over all seasons are:{closed_deals_invested_in_multiple_entreprenuers.shape[0]}') # 87 closed deals over the years for the multiple_entreprenuers
    #
    # the_amount_of_money_been_invested_on_multiple_entreprenuers = closed_deals_invested_in_multiple_entreprenuers['askedfor'].sum() # The_amount_of_money_been_invested_on_multiple_entreprenuers : 22,810,000
    print('*')

    # 7. In which category the dict_sharks invested their money?

    # In which industry does multiple entrepreneurs work on?
    # closed_deals = df.loc[df['deal'] == True, :]  # first condition
    # closed_deals_invested_in_multiple_entreprenuers = closed_deals.loc[closed_deals['multiple_entreprenuers'] == True,:]
    # result = closed_deals_invested_in_multiple_entreprenuers['category'].value_counts()
    # print('*')

    # 11. What is the ratio of investments of each shark choosing between multiple entrepreneurs VS individual entrepreneurs?
    res = ratio_of_investments_of_each_shark_choose_between_multiple_entrepreneurs_VS_individual_entrepreneur(all_the_deals_closed)
    two_bar_plot_shows_multiple_entrepreneurs_VS_individual_entrepreneur(res[0], res[1])
    print('*')

    # 20. How many “No”s and “Yes”s ( for investment ), each category got over the years ?
    # res = retrieving_the_amount_of_investments_and_non_investments_by_categories(df)
    # creating_bidirectional_bar_chart_by_categories(res)
    # print('*')

    # TODO : ask gil about the 2 strite lines - How to add?
    # Which industries that have gotten hotter / colder over the past 6 seasons?
    # Two conditions together :
    # res =which_industries_have_gotten_hotter_or_colder_over_6_seasons(df)
    # slope_chart_for_industries_have_gotten_hotter_or_colder_over_6_seasons(res)
    print('*')

    # valution_by_city:
    # res =df.groupby('valuation')['valuation']
    # print('*')

    # df = df.dropna(how='all')
    counting_the_number_of_entrepreneuers_in_a_group_for_pitching(df)
    print('*')

    # Which shark is known as the more willing to take risks? # TODO : continue with the risky shark + chart
    closed_deals = df.loc[df['deal'] == True, :]
    finding_the_shark_which_known_as_willing_to_takes_risky_investment(closed_deals)
    print('*')
    # What is the average investment over the seasons?
    groups_by_season = closed_deals.groupby('season')
    for season, askedfor_df_by_season in groups_by_season:
        # print(season)
        # print(askedfor_df_by_season)
        avg_investment_per_season_show = askedfor_df_by_season['askedfor'].mean()
        tatal_investment_per_season_show = askedfor_df_by_season['askedfor'].sum()
        print('*')

        # 22. Which shark is known investing in multiple entrepreneurs and in which field?
        getting_the_shark_name_investing_in_multiple_entrepreneurs_in_dif_fields(all_the_deals_closed)
        print('*')

        # 23. What is the average valuation of each shark willing to invest? ( over each season )
        #getting_avg_valuation_of_each_shark_willing_to_invest_each_season(all_the_deals_closed)
        #print('*')

    # ['deal', 'description', 'episode', 'category', 'entrepreneurs', 'location', 'website', 'askedfor', 'exchangeforstake', 'valuation', 'season', 'shark1', 'shark2', 'shark3', 'shark4', 'shark5', 'title', 'episode_season', '']
