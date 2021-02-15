import pandas as pd

"""
dflist = [pd.read_csv(f'google-{i}.csv', header=1, index_col = 'Month') for i in ('job',"hotel","nokia", "iphone", "coffee")]
google = dflist[0]
for df in dflist[1:]:
    print(google, df)
    google = google.set_index('Month').join(df.set_index("Month"))
print(google)"""
   
import matplotlib.pyplot as plt
import numpy as np

# Uniformly sample 50 x values between -2 and 2:
x = np.linspace(-2, 2, 50)

# Create an empty figure
fig, ax = plt.subplots()

# Plot y = x
ax.plot(x, x, label='$y=x$')

# Plot y = x^2
ax.plot(x, x**2, label='$y=x^2$')

# Plot y = x^3
ax.plot(x, x**3, label='$y=x^3$')

# Set the labels for x and y axes:
ax.set_xlabel('x')
ax.set_ylabel('y')

# Set the title of the figure
ax.set_title("Our First Plot -- Object-Oriented Style")

# Create a legend
ax.legend()
