import numpy as np
import pandas as pd
import dataframe_image as dfi
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import seaborn as sns

# creating 2 subplots - Mix ,Female , male : 1) gender presentation on shark tank - who gave a pitch
                                            # 2) gender presentation on shark tank and got funded


if __name__ == '__main__':

    df = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')

    usa = df[df['country']=='USA'].transpose()[1:4].reset_index()
    usa.columns = ['drinks', 'servings']

    fig = plt.figure(figsize=(16,6))
    fig.tight_layout(pad=5)

    # Creating a case-specific function to avoid code repetition
    def plot_vert_bar(subplot, y_min):
        plt.subplot(1,2,subplot)
        ax = sns.barplot(x='drinks', y='servings',
                         data=usa, color='slateblue')
        plt.title('Drink consumption in the USA', fontsize=30)
        plt.xlabel(None)
        plt.xticks(usa.index, ['Beer', 'Spirit', 'Wine'], fontsize=25)
        plt.ylabel('Servings per person', fontsize=25)
        plt.yticks(fontsize=17)
        plt.ylim(y_min, None)
        sns.despine(bottom=True)
        ax.grid(False)
        ax.tick_params(bottom=False, left=True)
        return None

    plot_vert_bar(1, y_min=80)
    plot_vert_bar(2, y_min=None)
    plt.show()