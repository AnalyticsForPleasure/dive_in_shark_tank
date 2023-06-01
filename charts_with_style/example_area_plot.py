import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

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
    print('*')

    # # display(df)
    # Medical  Surgical  Physician Services  Newborn  Maternity  Mental Health
    # 2011    26.80     21.74               13.10     9.38      12.10           4.33
    # 2012    24.97     19.58               12.45     8.18      10.13           3.73
    # 2013    25.69     20.70               12.75     8.79      10.76           3.78
    # 2014    24.07     21.09               10.79     6.75       8.03           3.75

    # plot
    ax = df.plot(kind='area', xticks=df.index, title='Overall, inpatient costs have decreased in 2011',
                 color=sns.color_palette("Blues")[::-1], figsize=(10, 6), ylabel='Cost (USD)')
    ax.legend(bbox_to_anchor=(1.07, 1.02), loc='upper left')  # move the legend
    ax.set_frame_on(False)  # remove all the spines
    ax.tick_params(left=False)  # remove the y tick marks
    ax.set_yticklabels([])  # remove the y labels
    ax.margins(x=0.5, y=0.5)  # remove the margin spacing

    # annotate
    for x, v in df.iterrows():
        cs = v.cumsum()[::-1]  # get the cumulative sum of the row and reverse it to provide the correct y position
        for i, a in enumerate(v[::-1]):  # reverse the row values for the correct annotation
            ax.annotate(text=f'${a:0.2f}', xy=(x, cs[i]))

    # Displaying the chart
    plt.show()