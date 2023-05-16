import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib_venn import venn2, venn2_circles

if __name__ == '__main__':
    pd.set_option('display.max_rows', 900)
    df_2 = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',
                         sheet_name='Sheet1')
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
    panda_df = pd.DataFrame(data=numpyArray,
                            index=["Barbara", "Mark", "Lori", "Robert", "Daymond", "Kevin"],
                            columns=["Equity investment agreement", "Convertible note agreement",
                                     "Revenue-sharing agreement", "Royalty agreement", "Loan agreement"])

    print('*')

    # sum of coloumns in a specific row of the dataframe
    panda_df['sum_of_agreements_for_each_shark'] = panda_df.iloc[:, :5].sum(axis=1)

    # sum of rows in the specific columns of the dataframe
    sum_of_row = panda_df.iloc[:panda_df.shape[0], :].sum(axis=0)
    panda_df.loc[panda_df.shape[0], 0:6] = sum_of_row

    # rename the index of a specific row:
    panda_df = panda_df.rename(index={6: 'sum of each agreement'})

    print('*')

    # https://towardsdatascience.com/visualizing-intersections-and-overlaps-with-python-a6af49c597d9

    # sum of coloumns in a specific row of the dataframe
    panda_df['sum_of_agreements_for_each_shark'] = panda_df.iloc[:, :5].sum(axis=1)

    # sum of rows in the specific columns of the dataframe
    sum_of_row = panda_df.iloc[:panda_df.shape[0], :].sum(axis=0)
    panda_df.loc[panda_df.shape[0], 0:6] = sum_of_row

    # rename the index of a specific row:
    panda_df = panda_df.rename(index={6: 'sum of each agreement'})

    print('*')

    # The total amount of agreements made by each shark:
    Barbara_total_investment = panda_df.iloc[0, :].to_list()
    Mark_total_investment = panda_df.iloc[1, :].to_list()
    Lori_total_investment = panda_df.iloc[2, :].to_list()
    Robert_total_investment = panda_df.iloc[3, :].to_list()
    Daymond_total_investment = panda_df.iloc[4, :].to_list()
    Kevin_total_investment = panda_df.iloc[5, :].to_list()

    # The  amount of total agreements made:
    Total_equity_investments_agreements_made_by_all_sharks = panda_df.iloc[:, 0].to_list()
    Total_convertible_note_agreements_made_by_all_sharks = panda_df.iloc[:, 1].to_list()
    Total_revenue_sharing_agreement_made_by_all_sharks = panda_df.iloc[:, 2].to_list()
    Total_royalty_agreement_made_by_all_sharks = panda_df.iloc[:, 3].to_list()
    Total_loan_agreement_made_by_all_sharks = panda_df.iloc[:, 4].to_list()

    venn2([set(Barbara_total_investment), set(Total_equity_investments_agreements_made_by_all_sharks)],
          set_colors=('#3E64AF', '#3EAF5D'),
          set_labels=('Total\ninvestments\n of Barbara',
                      'Total\n Equity investment \n  agreement'),
          alpha=0.75)
    venn2_circles([set(Barbara_total_investment),
                   set(Total_equity_investments_agreements_made_by_all_sharks)], lw=0.7)
    plt.show()

    ########################################################################################################################

    labels_sharks = ['Barbara',
                     'Mark',
                     'Lori',
                     'Robert',
                     'Daymond',
                     'Kevin']

    labels_agreements = ["Equity investment agreement",
                         "Convertible note agreement",
                         "Revenue-sharing agreement",
                         "Royalty agreement",
                         "Loan agreement"]

    c = ('#3E64AF', '#3EAF5D')

    # subplot indexes
    txt_indexes = [1, 7, 13, 19, 25]  # the index of each txt will be on the matrix 6 on 6.
                                      # Therefore   the 7,14,19,25 position would be the first position in each line.
                                      # 1+6 = 7 , 7+6=13, 13+6= 19, 19+6= 25
    # title_indexes = [2, 9, 16, 23, 30] # The index of the diagonal venn diagrams - We what to change this
    title_indexes = [1, 2, 3, 3, 4, 5 ]
    plot_indexes = [8, 14, 20, 26, 15, 21, 27, 22, 28, 29]

    #
    # # combinations of sets
    title_sets = [[set(Barbara_total_investment), set(Total_equity_investments_agreements_made_by_all_sharks)],
                   [set(Barbara_total_investment), set(Total_convertible_note_agreements_made_by_all_sharks)],
                   [set(Barbara_total_investment), set(Total_revenue_sharing_agreement_made_by_all_sharks)],
                   [set(Barbara_total_investment), set(Total_royalty_agreement_made_by_all_sharks)],
                   [set(Barbara_total_investment), set(Total_loan_agreement_made_by_all_sharks)]]

    plot_sets = [[set(Barbara_total_investment), set(Total_royalty_agreement_made_by_all_sharks)],
                 [set(Barbara_total_investment), set(Total_equity_investments_agreements_made_by_all_sharks)],
                 [set(Barbara_total_investment), set(Total_revenue_sharing_agreement_made_by_all_sharks)],
                 [set(Barbara_total_investment), set(Total_convertible_note_agreements_made_by_all_sharks)],
                 [set(Mark_total_investment), set(Total_royalty_agreement_made_by_all_sharks)],
                 [set(Mark_total_investment), set(Total_equity_investments_agreements_made_by_all_sharks)],
                 [set(Mark_total_investment), set(Total_convertible_note_agreements_made_by_all_sharks)],
                 [set(Lori_total_investment), set(Total_royalty_agreement_made_by_all_sharks)],
                 [set(Lori_total_investment), set(Total_equity_investments_agreements_made_by_all_sharks)],
                 [set(Daymond_total_investment), set(Total_royalty_agreement_made_by_all_sharks)]]

    fig, ax = plt.subplots(1, figsize=(16, 16))
    # Path number 1 :
    # plot texts - the for here below gives up the vertical names of each shark
    # for idx, txt_idx in enumerate(txt_indexes):
    #     plt.subplot(6, 6, txt_idx)
    #     plt.text(0.5, 0.5,
    #              labels_sharks[idx],  # labels[idx+1],
    #              ha='center', va='center', color='#1F764B')
    #     plt.axis('off')

    # Path number 2 :
    ##plot top plots (the ones with a title) - The for here below give us the diagonal venn diagrams
    for idx, title_idx in enumerate(title_indexes):
        plt.subplot(6, 6, title_idx)
        venn2(title_sets[idx], set_colors=c, set_labels = (' ', ' '))
        plt.title(labels_agreements[idx], fontsize=10, color='#1F4576')
        print('*')

    # Path number 3 :
    # plot the rest of the diagrams-  The for here below gives us the rest of the venn diagrams, under the diagonal venn diagrams.
    # for idx, plot_idx in enumerate(plot_indexes):
    #     plt.subplot(6, 6, plot_idx)
    #     venn2(plot_sets[idx], set_colors=c, set_labels = (' ', ' '))
    #
    #
    plt.show()
