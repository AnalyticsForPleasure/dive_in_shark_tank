import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools


if __name__ == '__main__':

    df = pd.read_csv('C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/part_one_3d.csv')  # six seasons
    print('*')

    data = df.loc[:6, 'BarbaraCorcoran':"KevinO'Leary"]
    res = data.to_numpy()

    # Set up the figure and the 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #coloring each series of sharks by different color: TODO: make it work
    group_colors_shark = ['skyblue', 'blue', 'paleturquoise', 'darkviolet', 'plum','lightgreen']


    # Set coordinates for the bars
    xpos, ypos = np.meshgrid(np.arange(6), np.arange(7))
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros_like(xpos)

    # Set dimensions for the bars (width, depth, height)
    dx = [0.05] * 42  # Adjust the length to match the number of bars (6x7=42)
    dy = [0.7] * 42
    dz = res.flatten()

    # Create the 3D bar plot
    #ax.bar3d(xpos, ypos, zpos, dx, dy, dz  ,color=shark_color)
    #ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=list(itertools.islice(shark_color, len(dz))))

    # # Plot the 3D bars for each group
    for pn in range(7):
        for i in range(6):
            ax.bar3d(xpos[i], ypos[pn, 0], zpos[pn, i], dx[i], dy[pn], dz[pn, i], color=group_colors_shark[i])


    # Set labels and title
    ax.set_xlabel('X',labelpad=12)
    ax.set_ylabel('Y',labelpad=12)
    ax.set_zlabel('Z',labelpad=12)
    ax.set_title('3D Bar Plot')

    # Set tick labels
    ax.set_xticks(np.arange(6) + 0.4)
    ax.set_yticks(np.arange(7) + 0.4)
    ax.set_xticklabels(['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond', "Kevin"])
    ax.set_yticklabels(['Health', 'Food', 'Lifestyle', 'Children', 'Fashion', 'Business Services', 'Fitness'])
    ax.set_zlabel('Number of investments made')

    plt.show()