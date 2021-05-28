def distance(strand_a, strand_b):
    hamming_distance = 0
    if len(strand_a) == len(strand_b):
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                hamming_distance += 1
        return hamming_distance
    else:
        raise ValueError("Sequences is not equal")


