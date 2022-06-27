from statistics import mean

all = {"q2c2" : False, "q3a1" : False, "q3b1" : False}

def check(q, a): 
    if q == "q2c2":
        all[q] = a == (24*60*60)*365
        return all[q]
    elif q == "q3a1":
        all[q] = a == mean([89,90,95])
        return all[q]
    elif q == "q3b1":
        all[q] = a == 3 * 120 - 120 / 10
        return all[q]

def checkall():
    print(all)