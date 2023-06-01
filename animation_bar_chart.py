import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

if __name__ == '__main__':
    n_frames = 10
    background_color = '#ffffff'  # '#95A4AD'
    bar_color = '#283F4E'
    gif_filename = 'bars'
    x = [1, 2, 3, 4, 5]

    coordinates_lists = [[0, 0, 0, 0, 0],
                         [10, 30, 60, 30, 10],
                         [70, 40, 20, 40, 70],
                         [10, 20, 30, 40, 50],
                         [50, 40, 30, 20, 10],
                         [75, 0, 75, 0, 75],
                         [0, 0, 0, 0, 0]]

    print('Creating charts\n')
    filenames = []
    plt.rcParams['axes.facecolor'] = 'none'

    for index in np.arange(0, len(coordinates_lists) - 1):
        y = coordinates_lists[index]
        y1 = coordinates_lists[index + 1]
        y_path = np.array(y1) - np.array(y)
        for i in np.arange(0, n_frames + 1):
            y_temp = (y + (y_path / n_frames) * i)
            # plot
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.set_facecolor(background_color)
            plt.bar(x, y_temp, width=0.4, color=bar_color)
            plt.title("Example for Shay")
            plt.ylim(0, 80)
            # remove spines
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.set_facecolor('#ffffff')
            # grid
            ax.set_axisbelow(True)
            ax.yaxis.grid(color='gray', linestyle='dashed', alpha=0.7)
            # build file name and append to list of file names
            filename = f'images/frame_{index}_{i}.png'
            filenames.append(filename)

            # last frame of each viz stays longer
            if i == n_frames:
                for i in range(5):
                    filenames.append(filename)
            # save img
            plt.savefig(filename, dpi=96, facecolor=background_color)
            plt.close()
    print('Charts saved\n')

    # Build GIF
    print('Creating gif\n')
    with imageio.get_writer(f'{gif_filename}.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    print('Gif saved\n')
    print('Removing Images\n')

    # Remove files
    for filename in set(filenames):
        os.remove(filename)
    print('DONE')