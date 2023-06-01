import numpy as np
import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns

# **************************************************************************************************************
# Function  name: relevant_columns_highlighter
# input: adding styles to our dataframe
# return value:
# ****************************************************************************************************************
def relevant_columns_highlighter(x):
    my_style = "color: #1E90FF;" \
               "font-weight: bold;"
    return [my_style] * len(x)

#"background-color: #1E90FF; "
# **************************************************************************************************************
# Function  name: which_industries_have_gotten_hotter_or_colder_over_6_seasons
# input:
# return value:
# ****************************************************************************************************************
def which_industries_have_gotten_hotter_or_colder_over_10_seasons(df_2):
    closed_deals_first_season = df_2.loc[(df_2['Deal'] == 'Yes') & (df_2['Season'] == 1)]  # 27 closed deals in season 1
    counter_1_season = closed_deals_first_season['Industry'].value_counts()
    #counter_1_season = counter_1_season.drop( ['Fitness Equipment'])  # dropping one category in order to compare to season 6
    counter_1_season = counter_1_season.reset_index(level=0)
    counter_1_season.rename(columns={counter_1_season.columns[0]: 'categories'}, inplace=True)
    counter_1_season.rename(columns={counter_1_season.columns[1]: 'Amount of investments by categories - Season 1'}, inplace=True)
    counter_1_season.sort_values(by='categories', inplace=True, ascending=False)
    #avg_valuation_1_season = closed_deals_first_season.groupby(['category'])['valuation'].mean()

    categories_in_season_1 = list(counter_1_season.loc[:, 'categories'])
    closed_deals_ten_season = df_2.loc[(df_2['Deal'] == 'Yes') & (df_2['Season'] == 10)]
    closed_deals_ten_season = closed_deals_ten_season.loc[closed_deals_ten_season['Industry'].isin(categories_in_season_1)]
    counter_6_season = closed_deals_ten_season['Industry'].value_counts()
    counter_6_season = counter_6_season.reset_index(level=0)
    counter_6_season.rename(columns={counter_6_season.columns[0]: 'categories'}, inplace=True)
    counter_6_season.rename(columns={counter_6_season.columns[1]: 'Amount of investments by categories - Season 10'}, inplace=True)

    counter_6_season.sort_values(by='categories', inplace=True, ascending=False)
    #avg_valuation_6_season = closed_deals_ten_season.groupby(['Industry'])['valuation'].mean()

    # Lets nerge the two data together:
    final_res = counter_1_season.merge(counter_6_season, on='categories', how='inner')
    print('*')

    # Adding styles to our dataframe ( coloring the column + removing the index column together)
    final_res = final_res.style.apply(func=relevant_columns_highlighter, subset=['categories']).hide_index()
    dfi.export(final_res, '../images/slope_chart/slope_chart.png')
    print('*')
    final_table_result = final_res.loc[[0,2, 4, 6, 7], :]
    print('*')
    return final_table_result



# Helper function for the -"slope_chart_for_industries_have_gotten_hotter_or_colder_over_6_seasons"

def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0], p2[0]], [p1[1], p2[1]], color='darkblue' if p1[1] - p2[1] > 0 else 'deepskyblue', marker='o',
                      markersize=6)  # coloring the line by condition
    ax.add_line(l)
    return l



# **************************************************************************************************************
# Function  name: slope_chart_for_industries_have_gotten_hotter_or_colder_over_6_seasons
# input:
# return value:
# ****************************************************************************************************************
def slope_chart_for_industries_have_gotten_hotter_or_colder_over_10_seasons(final_table):

    plt.style.use('seaborn')

    left_label = [str(c) + ' - '+ str(round(y)) for c, y in zip(final_table.categories, final_table['Amount of investments by categories - Season 1'])]
    right_label = [str(c) + ' - '+ str(round(y)) for c, y in zip(final_table.categories, final_table['Amount of investments by categories - Season 10'])]

    fig, ax = plt.subplots(1, 1, figsize=(14, 14), dpi=80)

    # Vertical Lines
    ax.vlines(x=1, ymin=1, ymax=18, color='black', alpha=1, linewidth=3, linestyles='dotted')
    ax.vlines(x=3, ymin=1, ymax=18, color='black', alpha=1, linewidth=3, linestyles='dotted')


    # Points
    ax.scatter(y=final_table['Amount of investments by categories - Season 1'], x=np.repeat(1, final_table.shape[0]), s=10, color='black', alpha=0.7)
    ax.scatter(y=final_table['Amount of investments by categories - Season 10'], x=np.repeat(3, final_table.shape[0]), s=10, color='black', alpha=0.7)
    print('*')

    # Line Segmentsand Annotation
    for p1, p2, c in zip(final_table['Amount of investments by categories - Season 1'], final_table['Amount of investments by categories - Season 10'], final_table['categories']):
        newline([1, p1], [3, p2])

        ax.text(1 - 0.05, p1, c + ' - ' + str(round(p1)), horizontalalignment='right', verticalalignment='center',
                fontdict={'size': 14})
        ax.text(3 + 0.05, p2, c + ' - ' + str(round(p2)), horizontalalignment='left', verticalalignment='center',
                fontdict={'size': 14})

    # 'Before' and 'After' Annotations
    ax.text(x=1 - 0.05, y=16.5, s='Season 1\n lead categories', horizontalalignment='right', verticalalignment='center',fontname='Franklin Gothic Medium Cond',weight='bold',
            fontdict={'size': 18, 'weight': 700})  # the position of the 'y' will be less the 18
    ax.text(x=3 + 0.05, y=16.5 ,s= 'Season 10 \n lead categories', horizontalalignment='left', verticalalignment='center',fontname='Franklin Gothic Medium Cond',weight='bold',
            fontdict={'size': 18, 'weight': 700})

    # Decoration
    ax.set_title("Which industries have gotten hotter or colder over 10 seasons?", fontdict={'size': 27},
                 weight='bold' ,
                 color = 'royalblue',
                 fontname='Franklin Gothic Medium Cond')
    #the next row is Extrimly  important
    ax.set(xlim=(0, 4), ylim=(0, 18), ylabel='Number of investments made by the sharks')
    ax.set_xticks([1, 3])
    ax.set_xticklabels(["Season 1\n lead categories", "Season 6 \n lead categories"])
    plt.yticks(np.arange(1, 1, 7), fontsize=12)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(.0)
    plt.gca().spines["bottom"].set_alpha(.0)
    plt.gca().spines["right"].set_alpha(.0)
    plt.gca().spines["left"].set_alpha(.0)
    plt.savefig('hot_vs_cold.jpg', dpi=250, bbox_inches='tight')
    plt.show()






if __name__ == '__main__':
    pd.set_option('display.max_rows', 900)
    df_2 = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')  # Ten seasons



    column_headers = list(df_2.columns.values)

    res = which_industries_have_gotten_hotter_or_colder_over_10_seasons(df_2)
    #slope_chart_for_industries_have_gotten_hotter_or_colder_over_10_seasons(res)
    print('*')