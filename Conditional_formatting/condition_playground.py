import pandas as pd
import numpy as np
import dataframe_image as dfi

#https://stackoverflow.com/questions/43596579/how-to-use-pandas-stylers-for-coloring-an-entire-row-based-on-a-given-column
np.random.seed(24)
df = pd.DataFrame({'A': np.linspace(1, 10, 10)})
print('*')
df = pd.concat([df, pd.DataFrame(np.random.randn(10, 4), columns=list('BCDE'))],axis=1)
df.iloc[0, 2] = np.nan

print('*')
def highlight_greaterthan(s, threshold, column):
    is_max = pd.Series(data=False, index=s.index)
    is_max[column] = s.loc[column] >= threshold
    return ['background-color: yellow' if is_max.any() else '' for v in is_max]


result = df.style.apply(highlight_greaterthan, threshold=1.0, column=['C', 'B'], axis=1)
dfi.export(result, filename='output_images/Example_coloring_specific_rows.png')