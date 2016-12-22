import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3
    balls of the same color were drawn in the first 3 draws.
    '''
    total = 0
    for _ in range(numTrials):
        bucket = [0, 0, 0, 0, 1, 1, 1, 1]
        drawn = random.sample(bucket, 3)
        if len(set(drawn)) == 1:
            total += 1
    return total/numTrials


print(drawing_without_replacement_sim(1000000))