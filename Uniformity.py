import math
from scipy import stats
from Input import get_tabular_input as inp, get_significance as get_sign


def set_intervals(ri, num_of_intervals, width):
    intervals = {}

    lower = 0
    for i in range(num_of_intervals):
        intervals[(lower, lower + width)] = 0
        lower = lower + width

    lower = 0
    for i in ri:
        for k in intervals.keys():
            if k[0] <= i < k[1]:
                intervals[k] += 1
                break

    return intervals


def variance(intervals, ei):
    sum = 0
    for key in intervals:
        sum += (ei - intervals[key]) ** 2

    return sum / ei


def run_uniformity(ri):
    if ri is None:
        ri = inp()
    a = get_sign()
    n = len(ri)
    m = int(math.sqrt(n))
    w = 1 / m
    ei = n / m
    intervals = set_intervals(ri, m, w)
    xo = variance(intervals, ei)
    x = float(stats.chi2.ppf(1 - a, m - 1))

    if xo < x:
        print("Conclusion:", "No se rechaza Ho por lo que el conjunto de valores ri es uniforme")
        return
    print("Conclusion:", "Se rechaza Ho y se acepta H1 por lo que el conjunto de valores ri no es uniforme")

    return None

