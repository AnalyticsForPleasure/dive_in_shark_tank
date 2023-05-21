import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':


        fig, ax = plt.subplots(figsize=(10, 6))

        shark_names = ['Mark', 'Daymond', 'Barbara', 'Robert', 'Kevin','Lori']
        shark_appearances = [73, 80, 51, 76,73,41]

        # This is the location for the annotated text
        i = 1.0
        j = 2000

        # Annotating the bar plot with the values (total death count)
        #for i in range(len(shark_appearances)):
               # plt.annotate(y=shark_appearances[i], (-0.1 + i, shark_appearances[i] + j))


        gradient = np.linspace(0, 1, len(shark_names)+1)
        gradient_colors = plt.cm.Blues(gradient)[1:6]

        ax.bar(shark_names, shark_appearances,color = gradient_colors)
        plt.title("Number of appearances on the show")

        plt.ylabel('number of appearances over the show') # Namimg the y axis

        plt.show()

