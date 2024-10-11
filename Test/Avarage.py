import math
from scipy import stats
from Input import get_tabular_input as inp, get_significance as get_sign

def calc_average(data):
    return sum(data)/len(data)

def run_avarage(ri = inp()):
    a = get_sign()
    n = len(ri)
    avg = calc_average(ri)
    li = 1/2 - stats.norm.ppf(1 - a/2) * (1/math.sqrt(12 * n))
    ls = 1/2 + stats.norm.ppf(1 - a/2) * (1/math.sqrt(12 * n))

    if li <= avg <= ls:
        return "No se rechaza Ho por lo que el conjunto de valores ri tiene una media de 0.5"
    return "Se rechaza Ho y se acepta H1 por lo que el conjunto de valores ri no tiene una media de 0.5"

if __name__ == '__main__':
    print(run_avarage())


