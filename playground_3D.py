import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':

    df = pd.read_csv('C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/part_one_3d.csv')  # six seasons
    print('*')

    data = df.loc[:6, 'BarbaraCorcoran':"KevinO'Leary"]
    res = data.to_numpy()

    # Set up the figure and the 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #coloring each series of sharks by different color: TODO: make it work
    shark_color = ['skyblue', 'blue', 'paleturquoise', 'darkviolet', 'plum']

    # Set coordinates for the bars
    xpos, ypos = np.meshgrid(np.arange(6), np.arange(7))
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)

    # Set dimensions for the bars (width, depth, height)
    dx = [0.2] * 42  # Adjust the length to match the number of bars (6x7=42)
    dy = [0.7] * 42
    dz = res.flatten()

    # Create the 3D bar plot
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz), #color=shark_color)


    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Bar Plot')

    # Set tick labels
    ax.set_xticks(np.arange(6) + 0.4)
    ax.set_yticks(np.arange(7) + 0.4)
    ax.set_xticklabels(['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond', "Kevin"])
    ax.set_yticklabels(['Health', 'Food', 'Lifestyle', 'Children', 'Fashion', 'Business Services', 'Fitness'])
    ax.set_zlabel('Number of investments by category')

    plt.show()