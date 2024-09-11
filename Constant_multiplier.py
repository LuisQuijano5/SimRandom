def constant_multiplier(x0, k, d, n):
    r = []
    x = []
    y = []
    x.append(x0)

    for i in range(n):
        y.append(k * x[i])
        x.append(int(raiz(d, y[i])))
        r.append(float('0.' + str(x[i+1])))

    return r


def raiz(d, y_0):
    y_str = str(y_0)

    if (len(y_str) - d) % 2 != 0:
        y_str = '0' + y_str
    mitad = len(y_str) // 2
    inicio = mitad - (d // 2)
    fin = inicio + d
    # Extraer los números del medio
    numeros_medio = y_str[inicio:fin]

    return numeros_medio

def run_cm():
    while(True):
        try:
            x = int(input('Ingresa la raiz: '))
            k = int(input('Ingresa la constante multiplicadora: '))
            d = len(str(x))
            n = int(input('Ingresa la cantidad de ri: '))
        except ValueError:
            print('Revisa tus inputs')
            continue

        print('RAICES: ')
        for i, t in enumerate(constant_multiplier(x, k, d, n)):
            print('raiz ' + str(i) + ': = ' + str(t))

        if input('Otra vez? S/N: ').upper() == 'N': break

if __name__ == '__main__':
    run_cm()
    # x = 91736
    # k = 30813
    # d = len(str(x))
    # n = 8
    #
    # print(constant_multiplier(x, k, d, n))