from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':

    df = pd.read_csv('C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/part_one_3d.csv')  # six seasons
    print('*')

    data = df.loc[:6, 'BarbaraCorcoran':"KevinO'Leary"]
    #res = data.to_numpy()
    #res_specific_column = data.iloc[:,'BarbaraCorcoran'].to_numpy()

    #Set up the figure and the 3D axis
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    sharks_names = data.columns.values
    print('*')

    zpos= [0]*14
    dx = [0.05] * 14  # Adjust the length to match the number of bars (6x7=42)
    dy = [0.7] * 14
    dz = data.to_numpy
    #for shark_color, z,shark_name in zip(['black', 'blue', 'darkcyan', 'darkorange','indigo','navy', 'gray'], [60,50,40, 30, 20, 10, 0],list(sharks_names)):
    #for shark_color, z in zip(['black', 'blue', 'darkcyan', 'darkorange','indigo','navy', 'gray'], [60,50,40, 30, 20, 10, 0]):
    for shark_color, z in zip(['navy', 'gray'], [60,50]):
        xpos = np.arange(7)
        ypos = data.loc[:, 'BarbaraCorcoran'].to_numpy() # different height
        print('*')

        # You can provide either a single color or an array. To demonstrate this,
        # the first bar of each set will be colored cyan.
        cs = [shark_color] * len(xpos)

        ax.bar(xpos, ypos, zs=zpos, zdir='y', color=cs, alpha=0.8)
        #ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=list(itertools.islice(shark_color, len(dz))))
        print('*')
    #
    # Set labels and title
    ax.set_xlabel('X',labelpad=12)
    ax.set_ylabel('Y',labelpad=12)
    ax.set_zlabel('Z',labelpad=12)
    ax.set_title('3D Bar Plot')

    # Set tick labels
    ax.set_xticks(np.arange(6) + 0.4)
    ax.set_yticks(np.arange(7) + 0.4)
    ax.set_xticklabels(['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond', "Kevin"])
    #ax.set_yticklabels(['Health', 'Food', 'Lifestyle', 'Children', 'Fashion', 'Business Services', 'Fitness'])
    ax.set_zlabel('Number of investments made')
    plt.show()




########################################################################################################################


# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# for c, z in zip(['r', 'g', 'b', 'y'], [30, 20, 10, 0]):
#     xs = np.arange(20)
#     ys = np.random.rand(20)
#
#     # You can provide either a single color or an array. To demonstrate this,
#     # the first bar of each set will be colored cyan.
#     cs = [c] * len(xs)
#     cs[0] = 'c'
#     ax.bar(xs, ys, zs=z, zdir='y', color=cs, alpha=0.8)
#
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
#
# plt.show()