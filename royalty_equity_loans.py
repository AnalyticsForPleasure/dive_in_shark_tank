import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


if __name__ == '__main__':
    pd.set_option('display.max_rows', 900)
    df_2 = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    df_2 = df_2.fillna(' ')
    print('*')

    print(df_2.columns.values)
    print('*')


    numpyArray = np.array([[10, 20, 10],
                           [20, 25, 15],
                           [12, 15, 19],
                           [12, 15, 19],
                           [12, 15, 19],
                           [12, 15, 19]])

    numpyArray = np.random.randint(20, size=(6, 5))
    print('*')
    panda_df = pd.DataFrame(data = numpyArray,
                            index = ["Barbara","Mark","Lori","Robert","Daymond","Kevin"],
                            columns = ["Equity investment agreement", "Convertible note agreement", "Revenue-sharing agreement","Royalty agreement","Loan agreement"])

    print('*')

    #sum of coloumns in a specific row of the dataframe
    panda_df['sum_of_agreements_for_each_shark'] = panda_df.iloc[:, :5].sum(axis=1)

    #sum of rows in the specific columns of the dataframe
    sum_of_row = panda_df.iloc[:panda_df.shape[0], :].sum(axis=0)
    panda_df.loc[panda_df.shape[0], 0:6] = sum_of_row

    # rename the index of a specific row:
    panda_df = panda_df.rename(index={6: 'sum of each agreement'})

    print('*')


#https://towardsdatascience.com/visualizing-intersections-and-overlaps-with-python-a6af49c597d9




    # The total amount of agreements made by each shark:
    Barbara_total_investment = panda_df.iloc[0,:].to_list()
    Mark_total_investment = panda_df.iloc[1, :].to_list()
    Lori_total_investment = panda_df.iloc[2, :].to_list()
    Robert_total_investment = panda_df.iloc[3, :].to_list()
    Daymond_total_investment = panda_df.iloc[4, :].to_list()
    Kevin_total_investment = panda_df.iloc[5, :].to_list()

    # The  amount of total agreements made:
    Total_equity_investments_agreements_made_by_all_sharks = panda_df.iloc[:,0].to_list()
    Total_convertible_note_agreements_made_by_all_sharks = panda_df.iloc[:,1].to_list()
    Total_revenue_sharing_agreement_made_by_all_sharks = panda_df.iloc[:, 2].to_list()
    Total_royalty_agreement_made_by_all_sharks = panda_df.iloc[:, 3].to_list()
    Total_loan_agreement_made_by_all_sharks = panda_df.iloc[:, 4].to_list()


    venn2([set(Barbara_total_investment), set(Total_equity_investments_agreements_made_by_all_sharks)],
           set_colors=('#3E64AF', '#3EAF5D'),
           set_labels=('Total\ninvestments\n of Barbara',
                       'Total\n Equity investment \n  agreement'),
                       alpha=0.75)
    venn2_circles([set(Barbara_total_investment), set(Total_equity_investments_agreements_made_by_all_sharks)], lw=0.7)
    plt.show()
