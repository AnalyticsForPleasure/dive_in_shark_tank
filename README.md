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


