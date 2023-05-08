# dive_in_shark_tank

Today we will work on the dataset taken from the kaggle website.
The dataset that we will dive into today would be on the “Shark Tank” TV show.
For some of you, who aren’t similar with the TV show “Shark Tank” series, the show is a show where entrepreneurs present their product or service to a panel of lenders or “sharks” for money. Then, they do a presentation in front of the panel of sharks. After the presentation, the entrepreneurs will seek money in return for a percentage of their company.

This mainstreaming of angel investment (  = a high net worth individual who invests their own money along with their time) in this entertaining format , gives us a bigger picture of how we can learn from the discussion of equity, funding, valuation and growth strategies.

Now, Let’s see a glimpse of the **angel investor** process

This data presents us with useful information about the show series taken on the ABC channel.
As we can see below, the dataset includes 18 columns 450 rows ( matrix of 450 *18 ). Each row gives us information about the next entrepreneur who is willing to succeed in the big world,


Here are the columns names:
'Deal'
'description'
 'Episode'
 'Category'
 'Entrepreneurs'
 'Location',
 'website' 
'Askedfor'
 'Exchangeforstake'
 'Valuation'
 'Season'
 'shark1', 'shark2' 'shark3' 'shark4' 'shark5'
 'Title'
 'Episode_season',
 'multiple_entreprenuers'







In the next chart I would like to know the number of investments made by the sharks in each season. Therefore, I would reveal this element and illustrate it by using  the pie chart.
We can notice, there is an increase in the number of investments made by the sharks as the TV show progressed over the seasons.
As we can see, the number of investments taken in the first and second season was 27 and 19 .
And on the opposite side, in the fifth season  and sixth season we can notice a big increase in numbers : 61 and 63.
Seasons 1+2  = 27+19 = 46
Seasons 5+6 = 61 + 63 = 124

In the next chart I want to dive into the information about the investing part of each shark getting into their pocket in order to invest in each entrepreneur project.
We can see here below in every waffle diagram the amount of money a specific shark invested in a relevant season vs the rest of investments made by the rest of the sharks.


![image](https://user-images.githubusercontent.com/28948369/234967869-da3aeb9b-3e4a-4710-9ff1-7a20b988f1ff.png)





# Analysis the new data 
As we go over the multiindex data we can notice an hierarchical indexing under the header of “ASK” and “DEAL” multiindex.
The “ASK” columns presents all the aspects ( Amount, acuity and valuation ) given by the entrepreneurs as they give their peches offer to the sharks.
The “DEAL”columns present the same aspects, but after a negotiation between the entrepreneurs and the sharks. Usually the sharks will try to “cut off “ the asking price valuation or reduce the amount of money they are willing to pay, In order to hedge their investments.

Therefore, I decided to drill down, and to focus on the negotiation part.

As we go over the multiindex data we can notice an hierarchical indexing under the header of “ASK” and “DEAL” multiindex.
The “ASK” columns presents all the aspects ( Amount, acuity and valuation ) given by the entrepreneurs as they give their peches offer to the sharks.
The “DEAL”columns present the same aspects, but after a negotiation between the entrepreneurs and the sharks. Usually the sharks will try to “cut off “ the asking price valuation or reduce the amount of money they are willing to pay, In order to hedge their investments.

Therefore, I decided to drill down, and to focus on the negotiation part.



The next thing we are willing to find out is out the investments made ny each shark upon the entrepreneurs. This mean we ae willing to know which shark preference to invest apon a solo entrepreneurs VS  multiple entreprenuers.

Therefore I wrote same code to anlaysis
```pyhton
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
              fontsize=16,
              weight='bold')
    # Naming the x and y axis
    plt.xlabel('Shark names', weight='bold')
    plt.ylabel('Number of investments', weight='bold')
    # Saving the plot as a 'png'
    plt.savefig('4BarPlot.png')
    # Displaying the bar plot
    plt.show()
```


![image](https://user-images.githubusercontent.com/28948369/236793307-0a116837-577a-4398-abc6-d9108eb23819.png)




