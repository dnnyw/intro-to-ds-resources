import pandas as pd
import numpy as np
from functions import *

temp_data = pd.read_csv("housing_subset.csv")


sample = [[6.968, 10.4], [5.965, 19.6], [3.563, 27.5], [7.853, 48.5]]


def rm_medv_errors(slope, intercept):
    fig, ax = plot_scatter(temp_data['rm'], temp_data['medv'])
    xlims = np.array([3.5,9])
    ax.plot(xlims, slope*xlims + intercept, color = 'black', lw= 2)
    for x, y in sample:
        ax.plot([x, x], [y, slope*x + intercept], color = 'r', lw= 2)
