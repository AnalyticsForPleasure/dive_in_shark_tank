import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':

    # df = pd.read_csv(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/auto_clean.csv')
    #
    # print(np.unique(df['body-style']))
    #
    # df['body-style1'] = df['body-style'].replace({'convertible': 1,
    #                                               'hardtop': 2,
    #                                               'hatchback': 3,
    #                                               'sedan': 4,
    #                                               'wagon': 5
    #                                               })
    #
    # gr = df.groupby("body-style1")["city-mpg", "price"].agg('median')
    #
    # x = gr.index
    # y = gr['city-mpg']
    # z = [0] * 5
    #
    # colors = ['skyblue', 'g', 'r', 'pink', 'coral']
    #
    # dx = [0.3] * 5
    # dy = [1] * 5
    # dz = gr['price']
    #
    # plt.figure(figsize=(0, 12))
    # ax = plt.axes(projection='3d')
    # ax.bar3d(x, y, z, dx, dy, dz, color=colors)
    # ax.set_xticklabels(['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond'] )
    # ax.set_xlim(0, 5.5)
    # ax.set_xlabel("Body Style", labelpad=12)
    # ax.set_ylabel("City MPG", labelpad=12)
    # ax.set_zlabel("Price", labelpad=12)
    # ax.set_title("Changes of price and body styles and city-mpg")
    # plt.show()
    #


    df = pd.read_csv('C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/part_one_3d.csv')  # six seasons

# Create sample data (6x6 matrix)
    #data = np.random.randint(low=1, high=33, size=(6, 6))
    data = df.to_numpy()
    # Set up the figure and the 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Set coordinates for the bars
    xpos, ypos = np.meshgrid(np.arange(6), np.arange(6))
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)
    print('*')
    # Set dimensions for the bars (width, depth, height)
    dx = dy = 0.8
    dz = data.flatten()

    # Create the 3D bar plot
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='skyblue')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Bar Plot')

    # Set tick labels
    ax.set_xticks(np.arange(6) + 0.4)
    ax.set_yticks(np.arange(6) + 0.4)
    ax.set_xticklabels(['A', 'B', 'C', 'D', 'E', 'F'])
    ax.set_yticklabels(['G', 'H', 'I', 'J', 'K', 'L'])

    # Show the plot
    plt.show()