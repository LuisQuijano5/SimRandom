from scipy import stats
from Input import get_tabular_input as inp, get_significance as get_sign


def calc_variance(data):
    avg = sum(data) / len(data)
    su = 0
    for i in data:
        su += (i - avg) ** 2
    return su / (len(data) - 1)


def run_variance(ri=inp()):
    a = get_sign()
    n = len(ri)
    avg = calc_variance(ri)
    ls = stats.chi2.ppf(1 - a / 2, n - 1) / (12 * (n - 1))
    li = stats.chi2.ppf(a / 2, n - 1) / (12 * (n - 1))

    if li <= avg <= ls:
        return "No se rechaza Ho por lo que el conjunto de valores ri tiene una varianza de 1/12"
    return "Se rechaza Ho y se acepta H1 por lo que el conjunto de valores ri no tiene una varianza de 1/12"


if __name__ == '__main__':
    print(run_variance())
