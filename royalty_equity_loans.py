import matplotlib.pyplot as plt
import numpy as np
import pandas as pd




# numpyArray = np.array([[10, 20, 10],
#                        [20, 25, 15],
#                        [12, 15, 19],
#                        [12, 15, 19],
#                        [12, 15, 19],
#                        [12, 15, 19]])

numpyArray = np.random.randint(12, size=(6, 3))
print('*')
panda_df = pd.DataFrame(data = numpyArray,
                        index = ["Barbara","Mark","Lori","Robert","Daymond","Kevin"],
                        columns = ["Royalty + Equity", "Equity + Loans", "Royalty + Loans"])


print('*')

if __name__ == '__main__':
    pd.set_option('display.max_rows', 900)
    df_2 = pd.read_excel(r'C:/Users/Gil/PycharmProjects/dive_into_shark_tank/Data/shark_tank_data.xlsx',sheet_name='Sheet1')
    df_2 = df_2.fillna(' ')
    print('*')

    #data =df_2.loc[:,'Barbara\nCorcoran':'Guest','# Sharks']

    print(df_2.columns.values)
    print('*')

