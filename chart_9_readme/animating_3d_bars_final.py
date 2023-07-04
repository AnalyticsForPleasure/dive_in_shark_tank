import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
import imageio

# In the line below, we used a global variable which will affect 2 element on the animation:
# 1) Height to the bar.
# 2) number of frames in each gif.
NUM_FRAMES_PER_GIF = 8


# We will  gradually update and increase the heights of bars on each frame "i" by ( input_heights / NUM_FRAMES_PER_GIF)/
# Each generated gif file refers to different industry.
def animate(i, input_heights):
    # Linear growth of the bar plot, the height get updated each call with extra 1/NUM_FRAMES_PER_GIF height.
    input_heights = i * (input_heights / NUM_FRAMES_PER_GIF)  # 0 < i < NUM_FRAMES_PER_GIF
    output = ax.bar3d(x=xx - bar_width / 2,
                      y=yy - bar_depth / 2,
                      z=np.zeros_like(xx),
                      dx=width_vec,
                      dy=depth_vec,
                      dz=input_heights,
                      color=color)

    ax.xaxis.set_ticks(x)
    ax.set_xticklabels(shark_names)
    ax.yaxis.set_ticks(y)
    ax.set_yticklabels(industries_names)
    ax.zaxis.set_ticks(np.arange(1, 35, step=5))

    ax.set_xlabel("Shark Name", fontsize=20, fontweight='heavy', fontname='Franklin Gothic Medium Cond')  # labelpad=12,
    ax.set_ylabel("Industry name", fontsize=20, fontweight='heavy',
                  fontname='Franklin Gothic Medium Cond')  # labelpad=12,
    ax.set_zlabel("Number of investments made", fontsize=25, fontweight='heavy',
                  fontname='Franklin Gothic Medium Cond')  # labelpad=17
    ax.set_title("Investments per Industry per shark", fontsize=36, fontweight='heavy',
                 fontname='Franklin Gothic Medium Cond')

    return output,


if __name__ == '__main__':
    shark_names = ['Barbra', 'Mark', 'Lori', 'Robert', 'Daymond', 'Kevin']
    industries_names = ['Health', 'Food', 'LifeStyle', 'Children']

    # Generating synthetic data:
    data = pd.read_csv('data/part_one_3d.csv')
    data = data.loc[1:4, 'BarbaraCorcoran':"KevinO'Leary"]

    # converting_dataframe_to_numpy
    actual_bar_heights = data.to_numpy()
    # actual_bar_heights = np.random.randint(low=1, high=10, size=(len(industries_names), len(shark_names)))
    print('*')
    df = pd.DataFrame(data=actual_bar_heights,
                      columns=shark_names,
                      index=industries_names)

    # The coordinates of the anchor point of the bars:
    x = [idx + 3 for idx, _ in enumerate(shark_names, start=1)]
    y = [idx + 3 for idx, _ in enumerate(industries_names, start=1)]

    xx_table, yy_table = np.meshgrid(x, y)

    zz = np.zeros((len(industries_names), len(shark_names)))
    # skyblue', 'dodgerblue', 'lightseagreen','palegreen','navy'
    colors = np.array(['skyblue', 'dodgerblue', 'lightseagreen', 'slategray', 'navy', 'lightsteelblue'] * len(
        industries_names)).reshape((4, 6))
    # dx, dy, dz : float or array-like
    # The width, depth, and height of the bars, respectively:
    bar_width = 0.3
    bar_depth = 0.5

    width_vec = [bar_width] * xx_table.shape[1]
    depth_vec = [bar_depth] * yy_table.shape[1]
    heights_vec = actual_bar_heights

    fig = plt.figure(figsize=(12, 12))
    ax = plt.axes(projection='3d')

    for idx, (xx, yy, heights, color) in enumerate(zip(xx_table, yy_table, actual_bar_heights, colors)):
        anim = FuncAnimation(fig,
                             func=animate,
                             frames=NUM_FRAMES_PER_GIF,
                             fargs=(heights,),
                             interval=100,
                             blit=True)
        anim.save(f'images/anim_{idx}.gif', writer='imagemagick')

    ########################################################################################################################
    # Stitching the gifs
    # List of GIF files to stitch together
    gif_files = ["images/anim_0.gif",
                 "images/anim_1.gif",
                 "images/anim_2.gif",
                 "images/anim_3.gif"]

    # Create a list to hold the frames of the stitched GIF
    frames = []

    # Iterate over the GIF files
    for gif_file in gif_files:
        # Read the frames from the current GIF file
        gif_frames = imageio.mimread(gif_file)
        # Extend the frames list with the frames from the current GIF file
        frames.extend(gif_frames)

    # Save the stitched GIF file
    output_file = "final_animation/stitched.gif"
    imageio.mimsave(output_file, frames, format='GIF',
                    duration=0.1)  # stiching the gifs
    print('*')
