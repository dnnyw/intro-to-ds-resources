from urllib.parse import _ResultMixinStr
import numpy as np
import math

keys = ["q1a1", "q1a2", "q1a3", "q1b1", "q1b2", "q1b3", "q21", "q22", "q3a1", "q3a2", 
        "q3b1", "q3b2", "q3c1", "q41", ]

#makes all the values False
result = dict.fromkeys(keys, False)

def check(q, a): 
    if q == "q1a1":
        result[q] = a == False
        return result[q]
    elif q == "q1a2":
        result[q] = a == True
        return result[q]
    elif q == "q1a3":
        result[q] = a == False
        return result[q]
    elif q == "q1b1":
        answer = 412 == 232 or 12 < 0 
        result[q] = a == answer
        return result[q]
    elif q == "q1b2":
        answer = not(21 != 20 and 320 <= 320) 
        result[q] = a == answer
        return result[q]
    elif q == "q1b3":
        answer = not((123 != 210 or 4 >= -3) and -21 <= -22)
        result[q] = a == answer
        return result[q]
    elif q == "q21":
        result[q] = a == "It's so fluffy!"
        return result[q]
    elif q == "q22":
        for value in a.values(): 
            if not value:
                result[q] = False
                return result[q]
        result[q] = True 
        return result[q]
    elif q == "q3a1":
        answer = [-1, (13 ** (1/2)), 31 // 2, 8 ** (3 * 27.2)] 
        result[q] = a == answer
        return result[q]
    elif q == "q3a2":
        answer = np.array(["Star-Lord", "Drax the Destroyer", "Groot", "Rocket", "Mantis"])
        temp = answer == a
        result[q] = all(temp)
        return temp
    elif q == "q3b1":
        answer = np.array(["Star-Lord", "Drax the Destroyer", "Groot II", "Rocket", "Mantis", "Gamora", "Yondu", "Nebula"])
        temp =  answer == a
        result[q] = all(temp)
        return temp
    elif q == "q3b2":
        answer = np.array(["Star-Lord", "Drax the Destroyer", "Groot II", "Rocket", "Mantis", "Nebula"])
        temp =  answer == a
        result[q] = all(temp)
        return temp
    elif q == "q3c1":
        result[q] = a == 12
        return result[q]
    elif q == "q41":
        result[q] = a == 3
        return result[q]
    

def checkall():
    print(result)
