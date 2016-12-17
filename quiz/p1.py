import random

def A():
    mylist = []
    r = 1

    if random.random() > 0.5:
        r = random.randint(1, 10)
    for i in range(r):
        random.seed(0)
        if random.randint(1, 10) > 3:
            number = random.randint(1, 10)
            mylist.append(number)
    return mylist


number = [7]
for i in range(100000):
    a = A()
    if number != a:
        print(a)

print(number)