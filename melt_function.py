import pandas as pd
import numpy as np
import dataframe_image as dfi  # Should install: "dataframe-image"

df_wide = pd.DataFrame(
    {"student": ["Andy", "Bernie", "Cindy", "Deb"],
     "school":  ["Z", "Y", "Z", "Y"],
     "english": [10, 100, 1000, 10000],  # eng grades
     "math":    [20, 200, 2000, 20000],  # math grades
     "physics": [30, 300, 3000, 30000]   # physics grades
     }
)

print('*')


output = df_wide.melt(id_vars=["student", "school"],
             var_name="cLaSs",  # rename
             value_name="gRaDe")  # rename

dfi.export(output, 'output_image1.png')
