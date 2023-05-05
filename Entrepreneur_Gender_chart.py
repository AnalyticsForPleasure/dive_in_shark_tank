import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


def creating_the_data_gender(df_2):

    genders_df = np.unique(df_2['Entrepreneur Gender'])
    index = [0]
    remove_element = np.array([0])
    genders_df_new = np.delete(genders_df, index)

    gender_counts = np.zeros(len(genders_df_new))  # initialize the array
    # in order to fill the array we will use a loop
    for n, gender in enumerate(genders_df_new):
        gender_counts[n] = 100 * (df_2['Entrepreneur Gender'] == gender).sum() / len(df_2)
    print('*')
    pos_gender_chart = np.arange(len(genders_df_new))

    return pos_gender_chart, gender_counts , genders_df_new


def horizontal_bar_plot_for_gender_enterpreneur(pos_gender, gender_counter , genders_df_new):

    fig, ax = plt.subplots(figsize=(12, 4))
    w = 0.6
    barlist = ax.bar(pos_gender, gender_counter, width=w, alpha=0.9)
    # ToDO:need to check the different between those 2 lines below
    ax.set_xticklabels(genders_df_new)
    #ax.set_xticklabels(genders_df_new, weight='heavy', fontsize=12)

    # Plot the metric
    ax.set_ylim([-2, 62])
    ax.set_xticks(pos_gender)
    ax.set_yticks(np.arange(0, 61, 20))
    ax.set_ylabel('Percent of entrepreneurs', fontsize=12)
    ax.tick_params(labelsize=12)

    ax.set_xticklabels([])
    xlim = ax.get_xlim()
    for X in pos_gender:  # Plot a horizontal line under each bar
        ax.plot([X - w / 2, X + w / 2], [0, 0], 'gray', alpha=0.25)
    ax.set_xlim(xlim)

    # Touch up the plot
    for b, c in zip(barlist, ['pink', 'skyblue', 'orange']):
        b.set_color(c)
    for n in np.arange(len(pos_gender_chart)):
        ax.text(gender_counter[n], 2, "{g}".format(g=genders_df[n]),fontsize=12, ha='center', color='w', weight='heavy')
        #ax.text(x[0]-0.18, 0.75, 'Female entrepreneurs', ha='left', va='bottom', fontsize=FS+2, alpha=1, rotation=90, color='w') # Check this line out
        
    mid = ax.get_xlim()[0]
    ##ax.set_title('Gender representation on Shark Tank', fontsize=12, weight='heavy')
    params = {'fontsize': 12, 'weight': 'heavy', 'ha': 'left', 'alpha': 0.9, 'color': 'gray'}
    y = 64
    ax.text(xlim[0] + 0.02, y, 'Gender representation on', fontdict=params)
    ax.text(xlim[0] + 0.879, y, 'Shark Tank', fontdict=params, style='italic')
    ax.text(xlim[-1] - 0.03, y, 'AnalyticsForPleasure', fontdict=params, fontsize=12, alpha=0.4, ha='right')

    plt.show()


if __name__ == '__main__':

    df_2 = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1') #
    df_2 = df_2.fillna(' ')
    print('*')

    #creating the Data (before adding a plot )

    pos_gender_chart ,gender_counts , genders_df = creating_the_data_gender(df_2)
    horizontal_bar_plot_for_gender_enterpreneur(pos_gender_chart ,gender_counts , genders_df )
    print('*')
