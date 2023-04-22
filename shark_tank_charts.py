import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


def getting_top_5_investments_made_by_a_shark_over_stack_bar_chart(table_result):
    # x- axis - all the names of the shark
    shark_names = table_result.loc[:, 'shark_name']
    categories = ['Toys and Games', 'Storage and Cleaning Products', 'Specialty Food', 'Novelties', 'Electronics']

    plt.figure(figsize=[15, 5])

    list_of_5_distinct_colors = plt.cm.Pastel2(range(5))  # "Pastel2" name of the palette

    # Initializing with zeros - zero for each shark
    offsets = np.zeros(10)
    for category, color in zip(categories, list_of_5_distinct_colors):
        data_of_specific_category = table_result.loc[:, category]
        plt.bar(shark_names, data_of_specific_category, bottom=offsets, color=color)

        # In each iteration the offsets gets updated since the bottom of the bar is getting higher
        offsets += data_of_specific_category

        for idx, (offset, value) in enumerate(zip(offsets, data_of_specific_category)):
            if value > 0:
                # Adding annotation and placing it at the specific place
                plt.annotate(text=f'{value:,.0f}$', xy=(idx - 0.35, offset-70000)) # 700000-is't isn't a shifting downside

    plt.xlabel("Shark name", fontsize=15, weight='bold')
    plt.ylabel("Amount of money invested in each \n category by each shark ( $ )", fontsize=12, weight='bold')
    plt.legend(["Toys and Games", "Storage and Cleaning Products", "Specialty Food", "Novelties", "Electronics"])
    plt.title("Top 5 industries investments made by a shark over the seasons", fontsize=20, weight='bold')
    plt.xticks(size=8.75)

    current_values = plt.gca().get_yticks()
    plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
    plt.show()


def pie_chart_which_illustrate_the_number_of_investments_each_season_over_the_years(res):
    amount_of_investments = list(res.loc[:, 'amount_of_investments_over_each_season'])  # _Tasks = [200, 400, 600])
    myLabels = list(res.loc[:, 'season_number'])
    explode = (0, 0.1, 0, 0, 0.2, 0)
    # figi, plt = plt.subplots(figsize =(6,6))
    c = ('cornflowerblue', 'lightsteelblue', 'slategrey', 'ghostwhite', 'lavender', 'darkblue')  # pie chart colors
    plt.pie(amount_of_investments, explode=explode, labels=myLabels, autopct='%1.1f%%', shadow=True, startangle=90,
            colors=c)
    plt.title('Number of investments made over each season', fontsize=20, weight='bold')
    plt.legend(amount_of_investments,
               title="Number of investments - each season ",
               loc="center left",
               fontsize=15,
               bbox_to_anchor=(1, 0, 0.5, 1))
    plt.show()


def two_bar_plot_shows_multiple_entrepreneurs_VS_individual_entrepreneur(individual_entre_df, multiple_entre_df):
    # Data to be plotted
    # In this chart we have 2 series: multiple_entrepreneur, individual_entrepreneur
    multiple_entrepreneur = list(multiple_entre_df.loc[:, 'counter_of_multiple_entrepreneur'])
    individual_entrepreneur = list(individual_entre_df.loc[:, 'counter_of_individual_entrepreneur'])

    X = np.arange(len(multiple_entrepreneur))
    # Passing the parameters to the bar function, this is the main function which creates the bar plot
    # Using X now to align the bars side by side
    plt.bar(X, multiple_entrepreneur, color='mediumspringgreen', width=0.20)
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

    # Giving the title for the plot
    # Number of investments made by each shark over \n team entrepreneur VS solo entrepreneur
    plt.title("Sharks' investments done through either Solo or with multiple entrepreneurs",
              fontsize=16,
              weight='bold')
    # Naming the x and y axis
    plt.xlabel('Shark names', weight='bold')
    plt.ylabel('Number of investments', weight='bold')
    # Saving the plot as a 'png'
    plt.savefig('4BarPlot.png')
    # Displaying the bar plot
    plt.show()




def creating_bidirectional_bar_chart_by_categories(final_table):
    # top_players_df = starting_players_with_avg_5_seasons.head(n=16)
    final_table
    #final_table.set_index('player_name', inplace=True)
    print('*')
    font_color = '#525252'
    hfont = {'fontname': 'Calibri'}
    facecolor = 'ghostwhite'
    color_red = 'lightskyblue'
    color_blue = 'royalblue'
    index = final_table ['selected_categories']
    column0 = final_table['counter_closed_deals']
    column1 = final_table['counter_unclosed_deals']
    title0 = 'Amount of closed deals by categories'
    title1 = 'Amount of unclosed deals by categories'

    fig, axes = plt.subplots(figsize=(10, 5), facecolor=facecolor, ncols=2, sharey=True)
    fig.tight_layout()

    axes[0].barh(index, column0, align='center', color=color_red, zorder=10)
    axes[0].set_title(title0, fontsize=18, pad=15, color=color_red, **hfont)
    axes[1].barh(index, column1, align='center', color=color_blue, zorder=10)
    axes[1].set_title(title1, fontsize=18, pad=15, color=color_blue, **hfont)

    # If you have positive numbers and want to invert the x-axis of the left plot
    axes[0].invert_xaxis()

    # To show data from highest to lowest
    plt.gca().invert_yaxis()

    axes[0].set(yticks=index, yticklabels=index)
    axes[0].yaxis.tick_left()
    axes[0].tick_params(axis='y', colors='white')  # tick color

    axes[1].set_xticks([5, 10, 15, 20, 25])
    axes[1].set_xticklabels([5, 10, 15, 20, 25])

    for label in (axes[0].get_xticklabels() + axes[0].get_yticklabels()):
        label.set(fontsize=13, color=font_color, **hfont)
    for label in (axes[1].get_xticklabels() + axes[1].get_yticklabels()):
        label.set(fontsize=13, color=font_color, **hfont)

    plt.subplots_adjust(wspace=0, top=0.85, bottom=0.1, left=0.18, right=0.95)

    filename = 'mpl-bidirectional'
    plt.savefig(filename+'.png', facecolor=facecolor)
    plt.show()

########################################################################################################################
# Helper function for the -"slope_chart_for_industries_have_gotten_hotter_or_colder_over_6_seasons"

def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0], p2[0]], [p1[1], p2[1]], color='red' if p1[1] - p2[1] > 0 else 'green', marker='o',
                      markersize=6)  # coloring the line by condition
    ax.add_line(l)
    return l




def slope_chart_for_industries_have_gotten_hotter_or_colder_over_6_seasons(final_table):

    left_label = [str(c) + ' - '+ str(round(y)) for c, y in zip(final_table.categories, final_table['counter_categories_season_1'])]
    right_label = [str(c) + ' - '+ str(round(y)) for c, y in zip(final_table.categories, final_table['counter_categories_season_6'])]

    fig, ax = plt.subplots(1, 1, figsize=(14, 14), dpi=80)

    # Vertical Lines
    ax.vlines(x=1, ymin=500, ymax=13000, color='black', alpha=0.5, linewidth=1, linestyles='dotted')
    ax.vlines(x=3, ymin=500, ymax=13000, color='black', alpha=1, linewidth=3, linestyles='dotted')


    # Points
    ax.scatter(y=final_table['counter_categories_season_1'], x=np.repeat(1, final_table.shape[0]), s=10, color='black', alpha=0.7)
    ax.scatter(y=final_table['counter_categories_season_6'], x=np.repeat(3, final_table.shape[0]), s=10, color='black', alpha=0.7)
    print('*')

    # Line Segmentsand Annotation
    for p1, p2, c in zip(final_table['counter_categories_season_1'], final_table['counter_categories_season_6'], final_table['categories']):
        newline([1, p1], [3, p2])

        ax.text(1 - 0.05, p1, c + ' - ' + str(round(p1)), horizontalalignment='right', verticalalignment='center',
                fontdict={'size': 14})
        ax.text(3 + 0.05, p2, c + ' - ' + str(round(p2)), horizontalalignment='left', verticalalignment='center',
                fontdict={'size': 14})

    # 'Before' and 'After' Annotations
    ax.text(1 - 0.05, 6, 'Season 1\n lead categories', horizontalalignment='right', verticalalignment='center',
            fontdict={'size': 18, 'weight': 700})
    ax.text(3 + 0.05, 6, 'Season 6 \n lead categories', horizontalalignment='left', verticalalignment='center',
            fontdict={'size': 18, 'weight': 700})

    # Decoration
    ax.set_title("Which industries have gotten hotter or colder over 6 seasons?", fontdict={'size': 22},  weight='bold' ,color = 'royalblue')
    ax.set(xlim=(0, 4), ylim=(0, 7), ylabel='Number of investments made by the sharks')
    ax.set_xticks([1, 3])
    #ax.set_xticklabels(["Season 1\n lead categories", "Season 6 \n lead categories"])
    plt.yticks(np.arange(1, 1, 7), fontsize=12)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(.0)
    plt.gca().spines["bottom"].set_alpha(.0)
    plt.gca().spines["right"].set_alpha(.0)
    plt.gca().spines["left"].set_alpha(.0)
    plt.show()





