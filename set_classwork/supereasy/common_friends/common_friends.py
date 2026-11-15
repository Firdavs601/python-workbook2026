def common(a, b):
    fri_a  = set(a)
    fri_b = set(b)
    return sorted(fri_a & fri_b)


def only_first(a, b):
    fri_a = set(a)
    fri_b = set(b)
    return sorted(fri_a - fri_b)