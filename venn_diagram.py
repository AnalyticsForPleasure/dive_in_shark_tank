#install the package "matplotlib-venn"
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



if __name__ == '__main__':
    df_2 = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')

    Course1=['A','B','C' ,'E','F','G','I','P','Q']
    Course2=['B','E','F','H','K','Q','R','S','T','U','V','Z']
    Course3=['C','E','G','H','J','K','O','Q','Z']


    #Method1: put two datasets directly
    venn2([set(Course1), set(Course3)])
    plt.show()

    #Method 2:
    venn2(subsets = (5, 8, 4))
    plt.show()

    #Method 3:  you need to pass a dictionary to the parameter subset.
    venn2(subsets = {'10': 5, '01': 8, '11': 4})
    plt.show()




    venn2([set(Course1), set(Course2)],
          set_labels=('Course1', 'Course2'),
          set_colors=('orange', 'darkgrey'),
          alpha = 0.8)
    plt.show()

    # venn2_circles([set(dataset1), set(dataset2)],
    #               linestyle='-.',
    #               linewidth=2,
    #               color='black')


