def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for
        the largest value in L then for the second largest, and so on to
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does
                not yield a set of multipliers such that the equation sums to 's'
    """
    L = sorted(L, reverse=True)
    large = {}
    summ = s
    for l in L:
        largest = 0
        for i in range(s+1):
            if l * i <= summ:
                largest = i
        summ -= l * largest
        large[l] = largest
    if summ == 0:
        return sum(large.values())
    else:
        return 'no solution'

print(greedySum([1, 2, 3, 4], 10))
print(greedySum([1], 20))
print(greedySum([10, 5, 1], 14))
print(greedySum([10, 5, 1], 11))
print(greedySum([10, 9, 8, 1], 17))
print(greedySum([10, 8, 5, 1], 13))
print(greedySum([15, 12, 4, 3, 1], 29))
print(greedySum([20, 10, 4, 3, 1], 21))
print(greedySum([21, 10, 8, 3, 1], 11))
print(greedySum([101, 51, 11, 2, 1], 3000))