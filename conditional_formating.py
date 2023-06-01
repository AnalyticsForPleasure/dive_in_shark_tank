import numpy as np
import pandas as pd
import dataframe_image as dfi



if __name__ == '__main__':

    # Example 1:
    df = pd.DataFrame({'A': [1,-2,3,-4,5,-6,7,-8,9,-10],
                       'B': np.random.rand(10),
                       'C': np.arange(10),
                       'D': [-5,np.nan,5,np.nan,-5,5,-5,np.nan,np.nan,5]})
    df

    #
    ########################################################################################################################
    df_1 = df.style.highlight_max()

    dfi.export(df_1, filename='example_1.png')


    ########################################################################################################################
    # Example 2: Format Table
    df_2 = df.style.set_properties(**{'background-color': 'dodgerblue',
                                      'color': 'white',
                                      'border-color': 'white',
                                      'border-width': '1px',
                                      'border-style': 'solid'})

    dfi.export(df_2, filename='Example_Format Table.png')

    ########################################################################################################################

    # Example 3: Highlight Specific Number under constrains
    def highlight_number(number):
        criteria = number == 7

        return ['background-color: springgreen' if i else '' for i in criteria] # Color kind - springgreen

    df_3 = df.style.apply(highlight_number)

    dfi.export(df_3, filename='Highlight_Specific_Number.png')

    ########################################################################################################################

    # Example 4: Make Negative Numbers Red
    # red if negative
    def color_negative_red(number):
        # returns a string with the css property 'color: red' for negative strings, black otherwise
        color = 'red' if number < 0 else 'black'
        return f'color: {color}'

    # looks at each value to find negative numbers
    df_4 =df.style.applymap(color_negative_red)
    dfi.export(df_4, filename='Make_Negative_Numbers_Red.png')

    ########################################################################################################################

    # Example 5: Highlight NAN
    df_5 =df.style.highlight_null(null_color='red')
    dfi.export(df_5, filename='Highlight_NAN.png')


    ########################################################################################################################

    # Example 8:Size Bars

    # size of bar corresponds to number in cell - in the specific column
    highlight = df.style.bar(subset=['A', 'B', 'C'], color='yellow')
    #highlight = df.style.bar(subset=['B'], color='yellow') <-- we can choose only one column

    # to html with style
    html = highlight.render()
    with open('highlight.html', 'w') as f:
        f.write(html)

    df_6 = highlight
    dfi.export(df_6, filename='size_of_bar_corresponds.png')

    ########################################################################################################################

    # Example 7: Highlight Max

    # highlight max
    # 0 = down the rows for each column
    # 1 = across the columns for each row
    df_7 =df.style.highlight_max(axis=0)
    dfi.export(df_7, filename='max_value_colored.png')


    ########################################################################################################################

    # Example 8: Highlight Min

    # 0 = down the rows for each column
    # 1 = across the columns for each row
    df_8 =df.style.highlight_min(axis=0)
    dfi.export(df_8, filename='min_value_colored.png')