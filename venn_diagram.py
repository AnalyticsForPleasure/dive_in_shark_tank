#install the package "matplotlib-venn"
from matplotlib_venn import venn3, venn3_circles
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



if __name__ == '__main__':
    df_2 = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',
                         sheet_name='Sheet1')


    groupA =['person1','person2','person3','person4','person5','person6','person7']
    groupB = ['person1','person2','person3', 'person8','person9']
    groupC = ['person1','person2', 'person4', 'person9','person10']

    print('*')
    #Let's now create 3 (each date one column) dataframe.
    dfA = pd.DataFrame(data=groupA,columns=['groupA'])
    dfB = pd.DataFrame(data= groupB,columns=['groupB'])
    dfC = pd.DataFrame(data =groupC,columns=['groupC'])
    print('*')

    # AB_overlap = A & B  #compute intersection of set A & set B
    # AC_overlap = A & C
    # BC_overlap = B & C
    # ABC_overlap = A & B & C
#https://medium.com/towards-data-science/how-to-create-and-beautify-venn-diagrams-in-python-331129bd4ed3
