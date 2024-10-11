def linear_congruential(c, k, m, x0):
    a = 1 + 4*k
    x = []
    x.append(x0)
    r = []
    for i in range(m):
        x.append((x[i] * a + c) % m)
        r.append(x[i+1]/(m-1))
    return r

def run_lc():
    while(True):
        try:
            c = int(input('Ingresa c: '))
            k = int(input('Ingresa k: '))
            m = int(input('Ingresa la cantidad de ri (m): '))
            x0 = int(input('Ingresa la semilla: '))
        except ValueError:
            print('Revisa tus inputs')
            continue

        print('Nums: ')
        for i, t in enumerate(linear_congruential(c, k, m, x0)):
            print('r' + str(i) + ': = ' + str(t))

        if input('Otra vez? S/N: ').upper() == 'N': break

if __name__ == '__main__':
    run_lc()
    # c =  73
    # k = 31
    # x0 = 97
    # m = 16
    # print(linear_congruential(c, k, m, x0))
def linear_congruential(c, k, m, x0):
    a = 1 + 4*k
    x = []
    x.append(x0)
    r = []
    for i in range(m):
        x.append((x[i] * a + c) % m)
        r.append(x[i+1]/(m-1))
    return r

def run_lc():
    while(True):
        try:
            c = int(input('Ingresa c: '))
            k = int(input('Ingresa k: '))
            m = int(input('Ingresa la cantidad de ri (m): '))
            x0 = int(input('Ingresa la raiz: '))
        except ValueError:
            print('Revisa tus inputs')
            continue

        print('RAICES: ')
        for i, t in enumerate(linear_congruential(c, k, m, x0)):
            print('raiz ' + str(i) + ': = ' + str(t))

        if input('Otra vez? S/N: ').upper() == 'N': break

if __name__ == '__main__':
    run_lc()
    # c =  73
    # k = 31
    # x0 = 97
    # m = 16
    # print(linear_congruential(c, k, m, x0))