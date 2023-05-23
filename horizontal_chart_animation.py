import pandas as pd
import plotly.express as px
import requests
import seaborn as sns
from bs4 import BeautifulSoup
import kaleido
import dataframe_image as dfi
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


if __name__ == '__main__':

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    print('*')


    closed_deals_first_season = df.loc[df['Deal'] == 'Yes',:]
    print('*')


    # Sample data
    categories = ['Category 1', 'Category 2', 'Category 3','Category 4', 'Category 5', 'Category 6']
    values1 = [10, 20, 15,8, 17, 25]
    values2 = [25, 15, 30, 11, 25, 19]
    values3 = [12, 18, 20, 21, 17, 13]


    # Set the positions of the bars on the y-axis
    y_pos = np.arange(len(categories))

    # Set the width of the bars
    width = 0.2

    plt.style.use('seaborn')  # This line is responsible for the gray background
    # Create the figure and axes
    fig, ax = plt.subplots()

    # Plotting the first set of bars
    ax.barh(y_pos - width, values1, height=width, color='blue', label='Series 1')

    # Plotting the second set of bars
    ax.barh(y_pos, values2, height=width, color='lightskyblue', label='Series 2')

    # Plotting the third set of bars
    ax.barh(y_pos + width, values3, height=width, color='steelblue', label='Series 3')

    # Set the y-axis labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories)

    # Set the x-axis label
    ax.set_xlabel('Values')

    # Set the title
    ax.set_title('Horizontal Bar Plot with Three Series')

    # Add a legend
    ax.legend()

    # Display the plot
    plt.show()