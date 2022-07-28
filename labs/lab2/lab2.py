import numpy as np
import math

keys = ["q1a1", "q1a2", "q1a3", "q1b1", "q1b2", "q1b3", "q21", "q22", "q3a1", "q3a2", 
        "q3b1", "q3b2", "q3c1", "q41", ]

#makes all the values False
all = dict.fromkeys(keys, False)

def check(q, a): 
    if q == "q1a1":
        all[q] = a == False
        return all[q]
    elif q == "q1a2":
        all[q] = a == True
        return all[q]
    elif q == "q1a3":
        all[q] = a == False
        return all[q]
    elif q == "q1b1":
        answer = 412 == 232 or 12 < 0 
        all[q] = a == answer
        return all[q]
    elif q == "q1b2":
        answer = not(21 != 20 and 320 <= 320) 
        all[q] = a == answer
        return all[q]
    elif q == "q1b3":
        answer = not((123 != 210 or 4 >= -3) and -21 <= -22)
        all[q] = a == answer
        return all[q]
    elif q == "q21":
        all[q] = a == "It's so fluffy!"
        return all[q]
    elif q == "q22":
        for value in a.values(): 
            if not value:
                all[q] = False
                return all[q]
        all[q] = True 
        return all[q]
    elif q == "q3a1":
        answer = [-1, (13 ** (1/2)), math.floor(31.2), 8 ** (3 * 27.2)] 
        all[q] = a == answer
        return all[q]
    elif q == "q3a2":
        answer = np.array(["Star-Lord", "Gamora", "Drax the Destroyer", "Groot", "Rocket", "Mantis"])
        all[q] = all(a == answer)
        return all[q]
    elif q == "q3b1":
        answer = np.array(["Star-Lord", "Gamora", "Drax the Destroyer", "Groot II", "Rocket", "Mantis", "Gamora", "Yondu", "Nebula"])
        all[q] = all(a == answer)
        return all[q]
    elif q == "q3b2":
        answer = np.array(["Star-Lord", "Gamora", "Drax the Destroyer", "Groot II", "Rocket", "Mantis", "Gamora", "Nebula", "Thor"])
        all[q] = all(a == answer)
        return all[q]
    elif q == "q3c1":
        all[q] = a == 12
        return all[q]
    elif q == "q3b2":
        guardians = np.array(["Star-Lord", "Gamora", "Drax the Destroyer", "Groot II", "Rocket", "Mantis", "Gamora", "Nebula", "Thor"])
        answer = [x for x in guardians if len(x) > 7]
        all[q] = a == len(answer)
        return all[q]
    

def checkall():
    print(all)
