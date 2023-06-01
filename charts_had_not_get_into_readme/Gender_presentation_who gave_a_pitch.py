import numpy as np
import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns

# creating 2 subplots - Mix ,Female , male : 1) gender presentation on shark tank - who gave a pitch
                                            # 2) gender presentation on shark tank and got funded


def creating_2_data_table_for_the_subplot(df):
    # Chart number 1  - : gender presentation on shark tank - who gave a pitch
    gender_shark_gave_a_pitch = df['Entrepreneur Gender'].value_counts()
    gender_shark_gave_a_pitch = gender_shark_gave_a_pitch.reset_index(level=0)
    gender_shark_gave_a_pitch.rename(columns={gender_shark_gave_a_pitch.columns[0]: 'Gender'}, inplace=True)
    gender_shark_gave_a_pitch.rename(columns={gender_shark_gave_a_pitch.columns[1]: 'Counter gender gave pitch'},
                                     inplace=True)
    # Chart Number 2: gender presentation on shark tank and got funded
    all_the_deals_closed = df.loc[df['Deal'] == 'Yes', :]
    res = all_the_deals_closed['Entrepreneur Gender'].value_counts()
    res = res.reset_index(level=0)
    res.rename(columns={res.columns[0]: 'Gender'}, inplace=True)
    res.rename(columns={res.columns[1]: 'Counter close deals by gender'}, inplace=True)
    print('*')




    # usa = df[df['country']=='USA'].transpose()[1:4].reset_index()
    # usa.columns = ['drinks', 'servings']
    #
    # fig = plt.figure(figsize=(16,6))
    # fig.tight_layout(pad=5)
    #
    # # Creating a case-specific function to avoid code repetition
    # def plot_vert_bar(subplot, y_min):
    #     plt.subplot(1,2,subplot)
    #     ax = sns.barplot(x='drinks', y='servings',
    #                      data=usa, color='slateblue')
    #     plt.title('Drink consumption in the USA', fontsize=30)
    #     plt.xlabel(None)
    #     plt.xticks(usa.index, ['Beer', 'Spirit', 'Wine'], fontsize=25)
    #     plt.ylabel('Servings per person', fontsize=25)
    #     plt.yticks(fontsize=17)
    #     plt.ylim(y_min, None)
    #     sns.despine(bottom=True)
    #     ax.grid(False)
    #     ax.tick_params(bottom=False, left=True)
    #     return None
    #
    # plot_vert_bar(1, y_min=80)
    # plot_vert_bar(2, y_min=None)
    # plt.show()




if __name__ == '__main__':


    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    print('*')

    creating_2_data_table_for_the_subplot(df)


