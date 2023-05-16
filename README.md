<p align="center">
  <img src="images/shark_tank_header.jpg" />
</p>


Today, we will be working with a dataset obtained from the Kaggle website. The dataset we are focusing on pertains to the popular TV show called "Shark Tank." For those unfamiliar with the show, it features entrepreneurs who present their products or services to a panel of lenders known as "sharks" in exchange for financial investment. The entrepreneurs deliver presentations to the panel, seeking monetary backing in return for a percentage of their company.

This televised format, showcasing angel investment (where high net worth individuals invest their own money and time), provides valuable insights into discussions on equity, funding, valuation, and growth strategies.

Now, let's take a brief look at the angel investor process.

The dataset we are working with contains information about the "Shark Tank" series aired on the ABC channel. It comprises 18 columns and 450 rows, forming a matrix of 450 * 18. Each row provides information about an aspiring entrepreneur venturing into the business world.

The column names include: 'Deal,' 'description,' 'Episode,' 'Category,' 'Entrepreneurs,' 'Location,' 'website,' 'Askedfor,' 'Exchangeforstake,' 'Valuation,' 'Season,' 'shark1,' 'shark2,' 'shark3,' 'shark4,' 'shark5,' 'Title,' 'Episode_season,' and 'multiple_entrepreneurs.'




We will start with the next chart I would like to know the number of investments made by the sharks in each season. Therefore, I would reveal this element and illustrate it by using  the pie chart.
We can notice, there is an increase in the number of investments made by the sharks as the TV show progressed over the seasons.
As we can see, the number of investments taken in the first and second season was 27 and 19 .
And on the opposite side, in the fifth season  and sixth season we can notice a big increase in numbers : 61 and 63.
Seasons 1+2  = 27+19 = 46
Seasons 5+6 = 61 + 63 = 124

![image](https://github.com/AnalyticsForPleasure/dive_into_shark_tank/assets/28948369/ba36aab0-718a-4310-b7cc-68b869f5a7c8)



One intriguing aspect we want to delve into is the level of investment made by each shark or guest on the show. Essentially, we aim to determine how much personal capital each individual is willing to invest in new entrepreneurial ideas. To shed light on this question, we conducted an analysis for each season, spanning from the first to the tenth. The chart below allows us to examine the percentage of investments made by a specific shark or guest in each season individua
![image](https://user-images.githubusercontent.com/28948369/234967869-da3aeb9b-3e4a-4710-9ff1-7a20b988f1ff.png)




The chart below displays the number of deals made by each shark in the panel over the years during entrepreneur presentations. Specifically, we are interested in determining the number of closed deals made by each shark, categorized by gender (male and female). For instance, Kavin had the highest number of deals with 132, this number doesn’t excluding those made with multiple entrepreneurs. Out of these, 93 deals (70.4%) were with male entrepreneurs, while the remaining 39 (29.6%) were with female entrepreneurs.

![image](https://github.com/AnalyticsForPleasure/dive_into_shark_tank/assets/28948369/cb3534ad-fd37-4580-bc62-2ae04acf3297)


Our next objective is to determine the number of investments made by each shark with regards to entrepreneurs. Specifically, we want to understand the sharks' preferences when it comes to investing in solo entrepreneurs versus multiple entrepreneurs.
Interestingly, we observe that all sharks show a clear inclination towards investing in companies that have multiple partners rather than those led by a single individual. They tend to allocate a higher number of investments to companies with several stakeholders compared to those primarily led by a single person.





![image](https://user-images.githubusercontent.com/28948369/236793307-0a116837-577a-4398-abc6-d9108eb23819.png)


The next thing that we would like to dive into is to find out for each deal which has been closed by each shark, what was the amount of equity settled during the negotiation process between the entrepreneur VS the shark. Therefore, we decided to add another element to the equation - for each closed deal by each shark we will divide the deals by the gender of the entrepreneur. For example : Mark Cuban, during 10 seasons of the show that has been aired on TV, he made 68 investment deals with entrepreneurs over the show. As we can notice below, The average equity (%) for a male entrepreneur was 28.6%, while the average equity (%) for a female entrepreneur was 26.4%.



![image](https://github.com/AnalyticsForPleasure/dive_into_shark_tank/assets/28948369/ecc19377-a3da-41f0-b224-ffd21aab5f29)

As we are aware, in each episode of every season, the sharks make multiple investment decisions to become stakeholders in various projects or companies. These companies operate in diverse industries such as toys and games, electronics, specialty food, and more.

In our upcoming analysis, we aim to gain a deeper understanding of the specific industries in which the sharks have chosen to invest with entrepreneurs. Furthermore, we have included the monetary amounts that each shark has decided to invest in these industries. For example, Daymond has invested his funds in three different fields: electronics (650,000 USD), novelties (500,000 USD), and specialty food (380 USD).

![image](https://github.com/AnalyticsForPleasure/dive_into_shark_tank/assets/28948369/8c45ac2a-fb30-445e-9eef-7cbd433ad536)
