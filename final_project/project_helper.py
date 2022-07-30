import pandas as pd
import numpy as np
from functions import *

from scipy import optimize
import functools

# <---- HELPER FUNCTIONS ---- > 

def minimize(f, start=None, smooth=False, log=None, array=False, **vargs):
    """Minimize a function f of one or more arguments.

    Args:
        f: A function that takes numbers and returns a number

        start: A starting value or list of starting values

        smooth: Whether to assume that f is smooth and use first-order info

        log: Logging function called on the result of optimization (e.g. print)

        vargs: Other named arguments passed to scipy.optimize.minimize

    Returns either:
        (a) the minimizing argument of a one-argument function
        (b) an array of minimizing arguments of a multi-argument function
    """
    if start is None:
        assert not array, "Please pass starting values explicitly when array=True"
        arg_count = f.__code__.co_argcount
        assert arg_count > 0, "Please pass starting values explicitly for variadic functions"
        start = [10] * arg_count
    if not hasattr(start, '__len__'):
        start = [start]

    if array:
        objective = f
    else:
        @functools.wraps(f)
        def objective(args):
            return f(*args)

    if not smooth and 'method' not in vargs:
        vargs['method'] = 'Powell'
    result = optimize.minimize(objective, start, **vargs)
    if log is not None:
        log(result)
    if len(start) == 1:
        return result.x.item(0)
    else:
        return result.x


# <----------- Plotting Functions ----------->

def plot_bar(categories, heights, x_label = "", y_label = "", title = "", plot_w = 8, plot_h = 5, **kwargs):
    '''Wrapper on matplotlib.pyplot to create barplots. 
    
    ###

    categories: (array-like) order will be the order that is listed on the plot.
    heights: (array-like) order will coresspond to the order in categories.
    x_label: (string) Label on the x-axis
    y_label: (string) Label on the y-axis 
    plot_w: (int) Width of plot
    plot_h: (int) Height of plot

    '''

    if len(categories) != len(heights):
        raise Exception("Length of categories and heights do not match")
    
    fig, ax = plt.subplots(1, 1, figsize = (plot_w, plot_h))
    ax.bar(x = categories, height = heights, **kwargs)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    return fig, ax  

def plot_histogram(data, bins = None, x_label = "", y_label = "", title = "", plot_w = 8, plot_h = 5, density = False, **kwargs):
    '''Wrapper on matplotlib.pyplot to create histograms. 
    
    ###

    data: (array-like) Data that will be plotted in the histogram
    x_label: (string) Label on the x-axis
    y_label: (string) Label on the y-axis 
    plot_w: (int) Width of plot
    plot_h: (int) Height of plot

    '''

    fig, ax = plt.subplots(1, 1, figsize = (plot_w, plot_h))
    ax.hist(x = data, bins = bins, density = density, edgecolor='black', **kwargs)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    return fig, ax  


def plot_scatter(x_data, y_data, x_label = "", y_label = "", title = "", plot_w = 8, plot_h = 5, **kwargs):
    '''Wrapper on matplotlib.pyplot to create histograms. 
    
    ###

    x_data: (array-like)
    y_data: (array-like)
    x_label: (string) Label on the x-axis
    y_label: (string) Label on the y-axis 
    plot_w: (int) Width of plot
    plot_h: (int) Height of plot

    '''
    fig, ax = plt.subplots(1, 1, figsize = (plot_w, plot_h))
    ax.scatter(x = x_data, y = y_data, **kwargs)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    return fig, ax  


def plot_line(x_data, y_data, x_label = "", y_label = "", title = "", plot_w = 8, plot_h = 5, **kwargs):
    '''Wrapper on matplotlib.pyplot to create a line plot. 
    
    ###

    x_data: (array-like)
    y_data: (array-like)
    x_label: (string) Label on the x-axis
    y_label: (string) Label on the y-axis 
    plot_w: (int) Width of plot
    plot_h: (int) Height of plot

    '''
    fig, ax = plt.subplots(1, 1, figsize = (plot_w, plot_h))
    ax.plot(x = x_data, y = y_data, **kwargs)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    return fig, ax  



# <----------- Linear Regression Functions ----------->


def standardize(an_array):
    return (an_array - np.mean(an_array))/np.std(an_array)








