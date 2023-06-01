import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.colors import LinearSegmentedColormap

# Based on the writen code here : https://stackoverflow.com/questions/70908289/filling-in-the-area-between-two-lines-with-a-custom-color-gradient
if __name__ == '__main__':

    x= np.arange(1,11,1)
    y1= np.array([27, 19, 28, 52, 57, 66, 65, 57, 65, 63])
    y2= np.repeat(0, 10)
    print('*')
    cm1 = LinearSegmentedColormap.from_list('Temperature Map', ['navy','skyblue'])

    polygon = plt.fill_between(x, y1, y2, lw=0, color='none')
    xlim = (x.min(), x.max())
    ylim = plt.ylim()
    verts = np.vstack([p.vertices for p in polygon.get_paths()])
    gradient = plt.imshow(np.linspace(0, 1, 256).reshape(-1, 1), cmap=cm1, aspect='auto', origin='lower',
                          extent=[verts[:, 0].min(), verts[:, 0].max(), verts[:, 1].min(), verts[:, 1].max()])
    gradient.set_clip_path(polygon.get_paths()[0], transform=plt.gca().transData)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()



