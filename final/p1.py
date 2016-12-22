import random

def p1_1():
    def sim(m):
        total = 0
        for j in range(m):
            total += random.choice([0, 1])
        return total/m

    print(sim(10000000))

p1_1()