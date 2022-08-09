import pandas as pd
import numpy as np
from functions import *

from scipy import optimize
import functools



temp_data = pd.read_csv("housing_subset.csv")


sample = [[6.968, 10.4], [5.965, 19.6], [3.563, 27.5], [7.853, 48.5]]

def standardize(array):
    return (array - np.mean(array)) / np.std(array)

def rm_medv_errors(slope, intercept):
    fig, ax = plot_scatter(temp_data['rm'], temp_data['medv'])
    xlims = np.array([3.5,9])
    ax.plot(xlims, slope*xlims + intercept, color = 'black', lw= 2)
    for x, y in sample:
        ax.plot([x, x], [y, slope*x + intercept], color = 'r', lw= 2)
        
    return fig, ax



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



rm = temp_data['rm']
medv =  temp_data['medv']

test1 = temp_data['dis']
test2 = temp_data['nox']

def get_cor(x, y):
    return np.corrcoef(x, y)[0][1]


def gs(x, y):
    return np.std(y)/np.std(x)*get_cor(x, y)

def gi(x, y):
    return np.mean(y) - np.std(y)/np.std(x)*get_cor(x, y)*np.mean(x)

def fpd(x, y, z):
    return gs(x,y) * z + gi(x,y)


def checkq2a(s, i):
    p = temp_data['rm']
    q = temp_data['medv']
    e = q - (s*p + i)
    return (np.mean(e**2))**0.5


def pmse(i, j, k):
    e = test2 - (i*(test1 - j)**2 + k)
    return (np.mean(e**2))**2


all = {'q1a':False,
    'q1b1':False,
    'q1b2':False,
    'q1b3':False,
    'q2a':False,
    'q2b':False,
    'q3a':False,
    'q3b':False}

def check(q, a):
    if q == 'q1a':
        all[q] = a(test1, test2) - get_cor(test1, test2) < 0.001
        return all[q]

    elif q == 'q1b1':
        all[q] = a(test1, test2) - gs(test1, test2) < 0.001
        return all[q]

    elif q == 'q1b2':
        all[q] = a(test1, test2) - gi(test1, test2) < 0.001
        return all[q]

    elif q == 'q1b3':
        all[q] = a(test1, test2, 10) - fpd(test1, test2, 10) < 0.000000001
        return all[q]

    elif q == 'q2a':
        all[q] = a(10, 20) - checkq2a(10, 20) < 0.000000001
        return all[q]

    elif q == 'q2b':
        all[q] = (a[0] - gs(rm, medv) < 0.0000000001) and (a[1] - gi(rm,medv) < 0.000000001)
        return all[q]

    elif q == 'q3a':
        all[q] = (a(1, 2, 3) - pmse(1, 2, 3) < 0.001)
        return all[q]

    elif q == 'q3b':
        all[q] = np.sum(a - minimize(pmse)) < 0.001
        return all[q]


def checkall():
    print(all)
