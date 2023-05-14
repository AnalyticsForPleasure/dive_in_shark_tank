#install the package "matplotlib-venn"
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



if __name__ == '__main__':

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



    # How to set colors and opacity ?
    venn2([set(Course1), set(Course2)],
          set_labels=('Course1', 'Course2'),
          set_colors=('Green', 'darkgrey'),
          alpha = 0.8)
    plt.show()


########################################################################################################################


    # How change the circles?
    vd2=venn2([set(Course1),set(Course2)],
               set_labels=('Course1', 'Course2'),
               set_colors=('Green', 'darkgrey'),
               alpha = 0.8)
    venn2_circles([set(Course1), set(Course2)],
                   linestyle='-.',
                   linewidth=2,
                    color='black')
    plt.show()

########################################################################################################################

    # How to change the siae of the label and numbers?
    vd2=venn2([set(Course1),set(Course2)],
              set_labels=('Course1', 'Course2'),
              set_colors=('Green', 'darkgrey'),
              alpha = 0.8)
    venn2_circles([set(Course1), set(Course2)],
              linestyle='-.',
              linewidth=2,
              color='black')
    for text in vd2.set_labels:  #change label size
        text.set_fontsize(29);
    for text in vd2.subset_labels:  #change number size
        text.set_fontsize(16)
    plt.show()
########################################################################################################################

    # How to add a title?
    vd2=venn2([set(Course1),set(Course2)],
              set_labels=('Course1', 'Course2'),
              set_colors=('Green', 'darkgrey'),
              alpha = 0.8)
    venn2_circles([set(Course1), set(Course2)],
                  linestyle='-.',
                  linewidth=2,
                  color='black')
    for text in vd2.set_labels:  #change label size
        text.set_fontsize(29);
    for text in vd2.subset_labels:  #change number size
        text.set_fontsize(16)
    plt.title('Venn Diagram for Course1 and Course2',
              fontname='Times New Roman',
              fontweight='bold',
              fontsize=20,
              pad=30,
              backgroundcolor='#cbe7e3',
              color='black',style='italic');
    plt.show()

########################################################################################################################