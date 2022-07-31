from csv import excel_tab
import pandas as pd
import numpy as np
from sqlalchemy import except_all
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
        start = [4] * arg_count
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


# <----- AUTOGRADER ------>

b = pd.read_csv('data/businesses.csv')
i = pd.read_csv('data/inspections.csv')
i_n = i.merge(right = b, how = 'inner', on = 'bid')
s = i_n[i_n['score'] >0]

# q4d1
temp = s['bid'].value_counts()
un = temp[temp >= 3].index

# q4d2
swi = np.array([])
for bid in un:
    subset = s[s['bid'] == bid]
    diff = max(subset['score']) - min(subset['score'])
    swi = np.append(swi, diff)

#q5 onwards

yr = s['rating']
rc = s['review_count']
p = s['price']
lrc = np.log(rc)


# q5c

def msey(s, i):
    error = yr - (s * lrc + i)
    return np.mean(error**2)


# q5d

bs = np.corrcoef(yr, lrc)[0][1]*np.std(yr)/np.std(lrc)
bi = np.mean(yr) - bs*np.mean(lrc)

def plot_q5d(slope, intercept):
    fig, ax = plt.subplots()
    ax.scatter(lrd, yr)
    lims = np.array([5, 9])
    ax.plot(lims, slope*lims + intercept)
    
#q5e

prices = ["$", "$$", "$$$", "$$$$"]
slopes = []
intercepts = []
for price in prices:
    data = s[s['price'] == price]
    rating = data['rating']
    review_num = np.log(data['review_count'])
    slope = np.corrcoef(rating, review_num)[1,0]*np.std(rating)/np.std(review_num)
    intercept = np.mean(rating) - slope*np.mean(review_num)
    slopes.append(slope)
    intercepts.append(intercept)
slopes = np.array(slopes)
intercepts = np.array(intercepts)

results = {'q1a':False,
    'q2a':False,
    'q2b':False,
    'q2c':False,
    'q3a':False,
    'q3b':False,
    'q3c1':False,
    'q4a':False,
    'q4c':False,
    'q4d1':False,
    'q4d2':False,
    'q4d3':False,
    'q5b':False,
    'q5c':False,
    'q5d':False,
    'q5e':False}


def check(q, a):
    if q == 'q1a':
        try:
            results[q] = (b.equals(a[0])) and (i.equals(a[1]))
        except:
            print('Something went wrong, try again!')
    elif q == 'q2a':
        try:
            bus = a[0]
            bid = a[1]
            results[q] = (bus == 607) and (bid == 658)
        except:
            print('Answer in wrong format!')
    elif q == 'q2b':
        try:
            results[q] = a == 'One Market Restaurant'
        except:
            print('Something went wrong, try again!')
    elif q == 'q2c':
        try:
            results[q] = a == 29
        except:
            print('Something went wrong, try again!')
    elif q == 'q3a':
        try:
            results[q] = a == b[b['name'] == 'One Market Restaurant']
        except:
            print("Something went wrong, try again!")
    elif q == 'q3b':
        try:
            results[q] = all(a == b[(b['rating'] <= 4) & (b['review_count'] > 1000)]['price'].value_counts())
        except:
            print("Something went wrong, try again!")
    elif q == "q3c1":
        try:
            temp = b[(b['latitude'] != -9999) & (b['longitude'] != -9999)]
            results[q] = temp.equals(a)
        except:
            print("Something went wrong, try again!")
    elif q == 'q4a':
        try:
            results[q] = s.equals(a)
        except:
            print("Something went wrong, try again!")
    elif q == 'q4c':
        try:
            results[q] = a == 'Mr Szechuan'
        except:
            print("Answer in wrong format!")
    elif q == 'q4d1':
        try:
            results[q] = all(a == un) or (len(a) == 334)
        except:
            print("Something went wrong, try again!")
    elif q == 'q4d2':
        try:
            results[q] = all(a == swi)
        except:
            print("Something went wrong, try again!")  
    elif q == 'q4d3':
        try:
            results[q] = a == 'Mr Szechuan'
        except:
            print("Something went wrong, try again!")
    elif q == 'q5b':
        try:
            results[q] = all(a == lrc)
        except:
            print("Something went wrong, try again!")
    elif q == 'q5c':
        try:
            results[q] = np.abs(msey(10,1) - a(10,1)) < 0.01
        except:
            print("Something went wrong, try again!")       
    elif q == 'q5d':
        try:
            results[q] =  (np.abs(a[0] - bs) < 0.001) and (np.abs(a[1] - bi) < 0.1)
            return [np.abs(a[0] - bs) < 0.001, np.abs(a[1] - bi) < 0.1]
        except:
            print("Something went wrong, try again!")
    elif q == 'q5e':
        try:
            results[q] = sum(np.abs(slopes - a[0])) < 1 and sum(np.abs(intercepts - a[1])) < 1
        except:
            print("Something went wrong, try again!")        
