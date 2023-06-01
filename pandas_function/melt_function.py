import pandas as pd
import numpy as np
import dataframe_image as dfi  # Should install: "dataframe-image"

df_wide = pd.DataFrame(
    {"student": ["Andy", "Bernie", "Cindy", "Deb"],
     "school":  ["Z", "Y", "Z", "Y"],
     "english": [60, 70, 80, 76],  # eng grades
     "math":    [89, 72, 76, 84],  # math grades
     "physics": [91, 94, 84, 82]   # physics grades
     }
)
dfi.export(df_wide, 'df_wide_image1.png')
print('*')


output = df_wide.melt(id_vars=["student", "school"],
             var_name="cLass",  # rename
             value_name="grade")  # rename
print('*')
dfi.export(output, 'output_image1.png')
