from itertools import groupby

def get_consecutives(array):
    # Enumerate and get differences between counter—integer pairs
    # Group by differences (consecutive integers have equal differences)  
    gb = groupby(enumerate(array), key=lambda x: x[0] - x[1])

    # Repack elements from each group into list
    all_groups = ([i[1] for i in g] for _, g in gb)

    # Filter out one element lists
    return list(filter(lambda x: len(x) > 1, all_groups))
    # [[8, 9], [1, 2, 3]]