import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':

    data = pd.read_csv('/Data/part_one_3d.csv')
    data = data.set_index('Industry')
    res = data.to_numpy()

    shark_names = ['Barbara ', 'Mark', 'Lori', 'Robert', 'Daymond', 'Kevin']
    industries_names = ['Health', 'Food', 'LifeStyle', 'Children','Fashion','Business Services',
                        'Fitness','Pet Products','Tech','Media','Travel','CleanTech','Autoemotive','Other' ]



    number_of_industries = 5

    df = pd.DataFrame(data=res[:number_of_industries],
                      columns=shark_names,
                      index=industries_names[:number_of_industries])
    res = df.to_numpy()
    print('*')
    # The coordinates of the anchor point of the bars:

    x = [idx + 0.5 for idx, _ in enumerate(shark_names, start=1)]
    y = [idx + 0.5 for idx, _ in enumerate(industries_names[:number_of_industries], start=1)]

    xx, yy = np.meshgrid(x, y)

    xx = xx.flatten()
    yy = yy.flatten()
    zz = [0] * len(industries_names[:number_of_industries]) * len(shark_names)

    colors = sorted(['skyblue', 'dodgerblue', 'lightseagreen','palegreen','navy'] * len(shark_names)) # 'lightsteelblue', 'black']

    # dx, dy, dz : float or array-like
    # The width, depth, and height of the bars, respectively:
    bar_width = 0.05
    bar_depth = 0.4

    width_vec = [bar_width] * len(xx)
    depth_vec = [bar_depth] * len(yy)
    heights_vec = res.flatten()

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
    ax.set_yticklabels(industries_names[:number_of_industries])

    ax.set_xlabel("Shark Name", labelpad=12)
    ax.set_ylabel("Industry name", labelpad=12)
    ax.set_zlabel("Number of times invested", labelpad=12)

    ax.set_title("Investments per Industry per shark")
    plt.show()
