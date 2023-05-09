import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if __name__ == '__main__':
    numpyArray = np.random.randint(20, size=(6, 5))
    gender_column = np.array(['F', 'M', 'F', 'M', 'M', 'M'])
    res = np.concatenate((gender_column.reshape(6, 1), numpyArray), axis=1)

    panda_df = pd.DataFrame(data=res,
                            index=["Barbara", "Mark", "Lori", "Robert", "Daymond", "Kevin"],
                            columns=["Gender", "Equity investment agreement", "Convertible note agreement",
                                     "Revenue-sharing agreement", "Royalty agreement", "Loan agreement"])

    plt.style.use('seaborn')  # This line is responsible for the gray background
    # Therefore we get in ax a list of subplots of two axis
    # you can unpack it, more easier:
    fig, all_6_axis = plt.subplots(nrows=1, ncols=6)

    for axis, shark_name in zip(all_6_axis, list(panda_df.index)):
        rects1 = axis.bar(1, 5, width=2, label='RMSE', color='lightblue')
        rects2 = axis.bar(3, 6, width=2, label='MAE')

        axis.set_title(f'Shark: {shark_name}')

    plt.show()
