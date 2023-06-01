import pandas as pd
import numpy as np

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
def get_categories_each_shark_invested_his_money(df_2):
    df_starting = pd.DataFrame({'shark_name': [],
                                'category': [],
                                'number_of_investments_per_category': [],
                                'amount_of_investments_per_category': []
                                })
    column_headers = list(df_2.columns.values)

    relevat_data = df_2.loc[:, 'Barbara\nCorcoran':'Guest']
    industry_column = df_2.loc[:,['Industry','DEAL_Amount']]
    final_table = pd.concat([industry_column,relevat_data ], axis=1)

    output = final_table.melt(id_vars=["Industry", "DEAL_Amount"],
                          var_name="choosen_shark"),  # rename
                          #value_name="choosen_shark")  # rename
    print('*')
    shark_name_list = []
    category_list = []
    investments_per_category_made_by_specific_shark_list = []
    sum_investments_per_category_made_by_specific_shark_list = []

    'Barbara\nCorcoran', 'Mark\nCuban', 'Lori\nGreiner', 'Robert Herjavec', 'Daymond\nJohn', "Kevin\nO'Leary", 'Guest'
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
    metrics_df = pd.pivot_table(top_investment_of_a_shark, values='Sum of money investments made', index='shark_name', columns='Category_selected')
    metrics_df.reset_index(inplace=True)
    metrics_df.fillna(0, inplace=True)
    #my_metrics_df = metrics_df.iloc[:,[0,7,15,22,23,24]] # Electronics(7),Novelties(15),Specialty_Food(22),Storage_and_Cleaning_Products(23),Toys_and_Games(24)
    print('*')
    return 4



if __name__ == '__main__':

    pd.set_option('display.max_rows', 500)
    df = pd.read_csv('C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_companies.csv')
    df_2 = pd.read_excel(r"C:\Users\Gil\PycharmProjects\building-blocks-python\data\shark_tank_data.xlsx",sheet_name='Sheet1')
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


    # The function :
    res = get_categories_each_shark_invested_his_money(df_2)
    print('*')