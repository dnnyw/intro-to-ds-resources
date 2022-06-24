import matplotlib.pyplot as plt
import numpy as np
import collections 
import pandas as pd


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








# <----------- Lecture Helper Functions ----------->



def r_scatter(r):
    """ Credit to Data 8 Textbook
    https://inferentialthinking.com/chapters/15/1/Correlation.html
    """

    plt.figure(figsize=(5,5))
    "Generate a scatter plot with a correlation approximately r"
    x = np.random.normal(0, 1, 1000)
    z = np.random.normal(0, 1, 1000)
    y = r*x + (np.sqrt(1-r**2))*z
    plt.scatter(x, y)
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)


def gen_categorical_data():
    """ No longer used """
    np.random.seed(101)
    letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D', 'F']
    probabilities = [0.03, 0.18, 0.19, 0.17, 0.13, 0.10, 0.07, 0.06, 0.04, 0.02, 0.01]
    grades = np.random.choice(a=letter_grades, p=probabilities, size=500)
    grade_counts = [collections.Counter(grades)[grade] for grade in letter_grades]
    letter_grades.reverse()
    grade_counts.reverse()
    return letter_grades, grade_counts


def gen_numerical_data():
    np.random.seed(101)
    grade_percents = np.random.beta(a = 7, b = 2, size = 500)
    return grade_percents


def get_galton_data():
    data_link = "https://raw.githubusercontent.com/data-8/textbook/main/assets/data/galton.csv"
    data = pd.read_csv(data_link, index_col = 0)
    mid_parent_height = data['midparentHeight'].values
    child_height = data['childHeight'].values
    return mid_parent_height, child_height


def get_census_data():
    data_link = 'http://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nc-est2019-agesex-res.csv'
    full_census_table = pd.read_csv(data_link)
