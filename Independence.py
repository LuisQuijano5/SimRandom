import math
from scipy import stats
from Input import get_tabular_input as inp, get_significance as get_sign


def count(data):
    co = 0
    last = -1
    was_larger = False
    for i in data:
        if last < i and not was_larger:
            co += 1
            was_larger = True
        if last > i and was_larger:
            co += 1
            was_larger = False
        last = i

    return co

def run_independence(ri):
    if ri is None:
        ri = inp()
    a = get_sign()
    n = len(ri)
    mco = (2 * n - 1) / 3
    vco = math.sqrt((16 * n - 29) / 90)
    co = count(ri)
    zo = abs((co - mco) / (vco))
    z = stats.norm.ppf(1 - a/2)

    if zo < z:
        print("Conclusion:", "No se rechaza Ho por lo que el conjunto de valores ri es independiente")
        return
    print("Conclusion:", "Se rechaza Ho y se acepta H1 por lo que el conjunto de valores ri no es independiente" )

    return None

