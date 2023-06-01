import matplotlib.pyplot as plt
import seaborn as sns
import dataframe_image as dfi
import numpy as np
import pandas as pd
from IPython.display import display
import openpyxl
import xlsxwriter

#The data.style.applymap() - function is used in pandas to apply a formatting or styling function element-wise on a DataFrame.
# Example number 1:

def highlight_cells(value):
    if value > 25:
        color = 'yellow'
    else:
        color = ''
    return 'background-color: {}'.format(color)

########################################################################################################################
#Example number 2:

    def highlight_cells(value, color_true, color_false, criteria):
        if value == criteria:
            color = color_true
        else:
            color = color_false
        return 'background-color: {}'.format(color)

if __name__ == '__main__':
    # create the DataFrame
    y1=[26.8,24.97,25.69,24.07]
    y2=[21.74,19.58,20.7,21.09]
    y3=[13.1,12.45,12.75,10.79]
    y4=[9.38,8.18,8.79,6.75]
    y5=[12.1,10.13,10.76,8.03]
    y6=[4.33,3.73,3.78,3.75]

    values = [y1, y2, y3, y4, y5, y6]
    labels = ["Medical", "Surgical", "Physician Services", "Newborn", "Maternity", "Mental Health"]
    years = [2011, 2012, 2013, 2014]
    data = dict(zip(labels, values))
    df = pd.DataFrame(data=data, index=years)



    df.style.highlight_min()
    print('*')
##################################################################################################


    #The data.style.applymap() - function is used in pandas to apply a formatting or styling function element-wise on a DataFrame.
    # Example number 1:

    df.style.applymap(highlight_cells)
    print('*')


########################################################################################################################
#Example number 2:


    df.style.applymap(highlight_cells, color_true = 'green', color_false = 'yellow', criteria = 2.55)
    print('*')

