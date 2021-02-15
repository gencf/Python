import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import *

def read_and_filter(filename, filter_limit):
    df = pd.read_csv(filename)
    filter = df[df["Y"] <= filter_limit]
    return filter


def fix_deformation(dataframe):
    a = 45*pi/180
    y = np.array(dataframe["Y"])
    x = np.array(dataframe["X"])
    y *= 2
    y -= 5
    x2 = x*cos(a) - y*sin(a)
    y2 = x*sin(a) + y*cos(a)
    x2 *= 100
    x2 += 1500
    x2 = x2[0:].round()
    return np.array([x2, y2]).T

    
def fit_and_predict(dataset, day):
    x = dataset[:, 0]
    y = dataset[:, 1]
    avgx = np.average(x)
    avgy = np.average(y)
    beta = np.sum([(x[i] - avgx)*(y[i] - avgy) for i in range(x.size)]) / np.sum([(x[j]-avgx)**2 for j in range(x.size)])
    alpha = avgy - beta*avgx
    predict = alpha + beta*day
    return (alpha, beta, predict)

  
def plot(dataset, alpha, beta, prediction, day):
    x = dataset[:, 0]
    y = dataset[:, 1] 
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel('Day')
    ax.set_ylabel('USD')
    ax.set_title("Exchange Rate")
    xline = [i for i in range(day+1)]
    yline = [alpha + beta*i for i in range(day+1)]
    ax.plot(xline, yline)

    
def test():
    df = read_and_filter("data.csv", 11)
    ds = fix_deformation(df)
    a,b,p = fit_and_predict(ds, 2500)
    plot(ds, a, b, p, 2500)


test()


