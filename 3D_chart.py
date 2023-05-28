import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':

    df = pd.read_csv('C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/part_one_3d.csv')
    print('*')
    shark_names = ['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond', 'Kevin']
    industries_names = ['Health', 'Food', 'LifeStyle', 'Children']
    actual_bar_heights = np.random.randint(low=1, high=10, size=(len(industries_names), len(shark_names)))

    df = pd.DataFrame(data=actual_bar_heights,
                      columns=shark_names,
                      index=industries_names)
    print('*')
    # The coordinates of the anchor point of the bars:

    x = [idx + 0.5 for idx, _ in enumerate(shark_names, start=1)]
    y = [idx + 0.5 for idx, _ in enumerate(industries_names, start=1)]

    xx, yy = np.meshgrid(x, y)

    xx = xx.flatten()
    yy = yy.flatten()
    zz = [0] * len(industries_names) * len(shark_names)

    colors = sorted(['skyblue', 'g', 'r', 'black'] * len(shark_names))

    # dx, dy, dz : float or array-like
    # The width, depth, and height of the bars, respectively:
    bar_width = 0.05
    bar_depth = 0.4

    width_vec = [bar_width] * len(xx)
    depth_vec = [bar_depth] * len(yy)
    heights_vec = actual_bar_heights.flatten()

    plt.figure(figsize=(0, 12))
    ax = plt.axes(projection='3d')
    ax.bar3d(x=xx - bar_width / 2,
             y=yy - bar_depth / 2,
             z=zz,
             dx=width_vec,
             dy=depth_vec,
             dz=heights_vec,
             color=colors)

    ax.xaxis.set_ticks(x)
    ax.set_xticklabels(shark_names)
    ax.yaxis.set_ticks(y)
    ax.set_yticklabels(industries_names)

    ax.set_xlabel("Shark Name", labelpad=12)
    ax.set_ylabel("Industry name", labelpad=12)
    ax.set_zlabel("Price", labelpad=12)

    ax.set_title("Investments per Industry per shark")
    plt.show()
