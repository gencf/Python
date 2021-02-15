import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("http://user.ceng.metu.edu.tr/~ceng240/data/railway.csv").set_index("Year")

length = np.array(df["Length"])
passenger = np.array(df["Passenger"])
(fig, ax) = plt.subplots()
ax.plot(length, passenger)
fig.savefig("7.1.png", format = "png")

length2 = [(i - length.min())/(length.max() - length.min()) for i in length]
passenger2 = [(i - passenger.min())/(passenger.max() - passenger.min()) for i in passenger]
(fig2, ax2) = plt.subplots()
ax2.plot(length2, passenger2)
fig2.show()
fig2.savefig("7.1_norm.png", format = "png")
    