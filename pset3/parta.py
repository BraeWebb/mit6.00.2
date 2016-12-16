import random

def simulateProp(numTrials, possible, unwanted, occurences, propbability):
    occurs = 0
    for _ in range(numTrials):
        selected = []
        for month in range(12):
            if random.random() <= propbability:
                selected.append(month)
        occur = True
        if not occurences:
            for month in possible:
                if month not in selected:
                    occur = False
            for month in unwanted:
                if month in selected:
                    occur = False
            if occur:
                occurs += 1
        else:
            happens = 0
            for month in possible:
                if month in selected:
                    happens += 1
            if happens >= occurences:
                occurs += 1
    return occurs/numTrials

print(simulateProp(1000000, [8, 9, 10], [], None, 0.1))
print(simulateProp(1000000, [8, 10], [9], None, 0.1))
print(simulateProp(1000000, [8, 9, 10], [], 1, 0.1))
print(simulateProp(1000000, [8, 9, 10], [], 2, 0.1))