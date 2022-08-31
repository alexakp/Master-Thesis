import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('inpainting/log/log_df.csv')

GLoss_arr = []
DLoss_arr = []

for v in df['epochs']:
    GLoss_arr.append(df.loc[v].at["GLoss"])
    DLoss_arr.append(df.loc[v].at["Dloss"])

plt.plot(GLoss_arr)
plt.plot(DLoss_arr)

plt.show()