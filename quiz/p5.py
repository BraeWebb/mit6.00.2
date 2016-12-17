def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    maximum = 0
    the_list = []
    count = 0
    for start in range(len(L)):
        for length in range(len(L) + 1 - start):
            if sum(L[start: length+start]) >= maximum:
                maximum = sum(L[start: length+start])
                the_list = L[start: length+start]
            count += 1
    print(count)
    print(the_list)
    return maximum


print(max_contig_sum([3, 4, -1, 5, -4]))
print(max_contig_sum([3, 4, -1, 5, -4, 100, 23, 43, 56, 2,-213, -3, 1,23,22000, -2345, 213, 12]))
print(max_contig_sum([3, 4, -8, 15, -1, 2]))