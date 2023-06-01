import numpy as np
import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines




# **************************************************************************************************************
# Function  name: ratio_of_investments_of_each_shark_choose_between_multiple_entrepreneurs_VS_individual_entrepreneur
# input:
# return value:
# ****************************************************************************************************************
def ratio_of_investments_of_each_shark_choose_between_multiple_entrepreneurs_VS_individual_entrepreneur(all_the_deals_closed):

    mapping = {True: 'individual entrepreneur',
               False: 'multiple entrepreneurs'}

    all_the_deals_closed['kind_of_entrepreneurs'] = all_the_deals_closed['multiple_entreprenuers'].apply(lambda x: mapping[x])
    filter_data_individual = all_the_deals_closed.loc[all_the_deals_closed['kind_of_entrepreneurs'] == 'individual entrepreneur', :]
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
    dfi.export(individual_entrepreneur_df, '../images/individual_vs_multi/individual_entrepreneur_df.png')
    print('*')

    return individual_entrepreneur_df, multiple_entrepreneur_df

# **************************************************************************************************************
# Function  name: two_bar_plot_shows_multiple_entrepreneurs_VS_individual_entrepreneur
# input:
# return value:
# ****************************************************************************************************************

def two_bar_plot_shows_multiple_entrepreneurs_VS_individual_entrepreneur(individual_entre_df, multiple_entre_df):
    # Data to be plotted
    # In this chart we have 2 series: multiple_entrepreneur, individual_entrepreneur
    multiple_entrepreneur = list(multiple_entre_df.loc[:, 'counter_of_multiple_entrepreneur'])
    individual_entrepreneur = list(individual_entre_df.loc[:, 'counter_of_individual_entrepreneur'])

    X = np.arange(len(multiple_entrepreneur))
    plt.style.use('seaborn')  # This line is responsible for the gray background
    # Passing the parameters to the bar function, this is the main function which creates the bar plot
    # Using X now to align the bars side by side
    plt.bar(X, multiple_entrepreneur, color='midnightblue', width=0.20)
    plt.bar(X + 0.25, individual_entrepreneur, color='lightskyblue', width=0.20)

    # Creating the legend of the bars in the plot ( This time 2 legends )
    plt.legend(['Multiple entrepreneurs', 'Solo entrepreneur'])


    # Overriding the x axis with the sharks names
    list_of_sharks = list(multiple_entre_df.loc[:, 'chosen_shark'])
    plt.xticks([i + 0.25 for i in range(multiple_entre_df.shape[0])], list_of_sharks)

    # # This is the location for the annotated text
    i = 1.0
    j = 0.25

    # Annotating the bar plot with the values (multiple_entrepreneur count)
    for i in range(len(multiple_entrepreneur)):
        plt.annotate(multiple_entrepreneur[i], (-0.05 + i, multiple_entrepreneur[i] + j))
    # Annotating the bar plot with the values (individual_entrepreneur count)
    for i in range(len(individual_entrepreneur)):
        plt.annotate(individual_entrepreneur[i], (i + 0.2, individual_entrepreneur[i] + j))


    # Adding the labels over the 2 series of the bar chart:
    plt.text(x=0.20, y=0.75,s= 'Solo', ha='left', va='bottom', fontsize=12, alpha=1, rotation=90, color='w',weight='bold')
    plt.text(x=-0.05, y=0.5, s='Multiple', ha='left', va='bottom', fontsize=12, alpha=1, rotation=90, color='w',weight='bold')

    for n in np.arange(len(individual_entrepreneur)):
        plt.text(x=n+1.22, y=0.75,s= 'Solo', ha='left', va='bottom', fontsize=12, alpha=1, rotation=90, color='w',weight='bold')
        plt.text(x=n+0.95, y=0.5, s='Multiple', ha='left', va='bottom', fontsize=12, alpha=1, rotation=90, color='w',weight='bold')

        # for n in np.arange(len(pos_gender_chart)):
        #     ax.text(x=pos_gender_chart[n], y=3.5, s="{g}".format(g=genders_df_new[n]), va='bottom', fontsize=12, # this line is correct
        #             ha='center', color='w', weight='heavy', alpha=1)
    # Giving the title for the plot
    # Number of investments made by each shark over \n team entrepreneur VS solo entrepreneur
    plt.title("Sharks' investments done through either Solo or with multiple entrepreneurs",
              fontsize=25,
              weight='bold',
              fontname='Franklin Gothic Medium Cond')
    # Add in title and subtitle

    # Naming the x and y axis
    plt.xlabel('Shark names', weight='bold',fontsize=16)
    plt.ylabel('Number of investments', weight='bold',fontsize=16)
    # Saving the plot as a 'png'
    plt.savefig('individual_vs_multi.png')
    # Displaying the bar plot
    plt.show()





if __name__ == '__main__':
    df = pd.read_csv('/Data/shark_tank_companies.csv')
    all_the_deals_closed = df.loc[df['deal'] == True, :]
    location_of_all_deals_closed = all_the_deals_closed['location'].value_counts()  # 19 closing deals were closed in L.A location
    print(f'The deals were closed over the states at:{location_of_all_deals_closed}')

    all_the_deals_closed = df.loc[df['deal'] == True, :]
    all_the_deals_closed['Shark_which_invested'] = np.random.randint(1, 11, size=251)
    # print('*')
    #
    # #instead of writing the entire sharked  hard coded, we will write the coded this way:
    shark_columns = [f'shark{i}' for i in range(1, 6)]
    shark_names = np.unique(df[shark_columns])
    dict_sharks = dict(zip(range(len(shark_names)), shark_names))
#
    all_the_deals_closed['chosen_shark'] = all_the_deals_closed['Shark_which_invested'].map(dict_sharks)
    print('*')
     #11. What is the ratio of investments of each shark choosing between multiple entrepreneurs VS individual entrepreneurs?
    res = ratio_of_investments_of_each_shark_choose_between_multiple_entrepreneurs_VS_individual_entrepreneur(all_the_deals_closed)
    two_bar_plot_shows_multiple_entrepreneurs_VS_individual_entrepreneur(res[0], res[1])
    print('*')
