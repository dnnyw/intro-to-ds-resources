
# Make sure to download the data before running this python file

import numpy as np
import pandas as pd


all = {'q1a':False ,
    'q1b':False ,
    'q1c':False ,
    'q1d':False ,
    'q2a':False ,
    'q2b':False ,
    'q2c':False ,
    'q2d':False ,
    'q2e':False ,
    'q3a2':False ,
    'q4a':False
    }


temp = pd.read_csv('raw_compensation.csv')
temp_p = temp['Total Pay']
temp_d = temp_p - np.mean(temp_p)
temp_sq = temp_d**2
temp_sd = np.std(temp_p)
temp_n = temp_d/temp_sd

def check(q, a):
    if q == 'q1a':
        all[q] = (a > 11.44) and (a < 11.5)
        return all[q]
    elif q == 'q1b':
        all[q] = sum(np.abs(a.values - temp_d.values) < 1) == 102
        return all[q]
    elif q == 'q1c':
        all[q] = sum(np.abs(a.values - temp_sq.values) < 1) == 102
        return all[q]
    elif q == 'q1d':
        all[q] = np.abs(a - temp_sd) < 1
        return all[q]
    elif q == 'q2a':
        all[q] = a == 20
        return all[q]
    elif q == 'q2b':
        all[q] = a == 2**(.5) / 2 * 100 
        return all[q]    
    elif q == 'q2c':
        all[q] = a("aeiou") == ""
        return all[q]
    elif q == 'q2d':
        all[q] = a(temp_p) == np.mean(temp_p)
        return all[q]
    elif q == 'q2e':
        all[q] = a(temp_p) == np.std(temp_p)
        return all[q]
    elif q == 'q3a2':
        all[q] = a == 4/102
        return all[q]
    elif q == 'q4a':
        all[q] = sum(a(temp_p) == temp_n) == 102
        return all[q]


def checkall():
    print(all)
