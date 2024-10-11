
def productos_medios(x_0,x_1,ri_num):
    y_results = []
    x_results = []
    ri_results = []

    d = len(str(x_0))

    for i in range(ri_num):
        y = x_0 * x_1

        x_0 = x_1
        x_1 = raiz(d, y)

        if(len(str(x_1)) < d):
            x_results.append("x_" + str(i + 2) + " = 0" + str(x_1))
            ri_results.append("r_" + str(i + 1) + " = 0.0" + str(x_1))
        else:
            x_results.append("x_" + str(i + 2) + " = " + str(x_1))
            ri_results.append("r_" + str(i + 1) + " = 0." + str(x_1))

        y_results.append("y_" + str(i) + " = "+str(y))

    print(y_results)
    print()
    print(x_results)
    print()
    print(ri_results)



def raiz(d, y_0):
    d = d
    y_str = str(y_0)

    if (len(y_str)-d) % 2 != 0:
        y_str = '0' + y_str

    # Calcular el índice de inicio para extraer los números del medio
    mitad = len(y_str) // 2
    inicio = mitad - (d // 2)
    fin = inicio + d

    # Extraer los números del medio
    numeros_medio = y_str[inicio:fin]

    return int(numeros_medio)


def run_lc():
    while(True):
        try:
            ri_num = int(input("Ingrese lo cantidad de ri: "))
            x_0 = int(input("Ingrese x_0: "))
            x_1 = int(input("Ingrese x_1: "))
        except ValueError:
            print('Revisa tus inputs')
            continue

        productos_medios(x_0, x_1, ri_num)
        if input('Otra vez? S/N: ').upper() == 'N': break

if __name__ == '__main__':
    run_lc()