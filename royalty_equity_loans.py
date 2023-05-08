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