import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://user.ceng.metu.edu.tr/~ceng240/data/olives.csv").set_index("Year")

filter = np.array(df[df["Olive"] > df["Olive"].mean()])
year = np.array(df[df["Olive"] > df["Olive"].mean()].index)

(fig, ax) = plt.subplots()
ax.plot(year, filter)
fig.savefig("7.2.png", format = "png")
print(year, olive, df["Olive"].mean(), filter)