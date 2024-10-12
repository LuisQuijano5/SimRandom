
def cuadrados_medios(ri_num, x_0):
    d = len(str(x_0))
    ri = []
    x_new = 0
    y = x_0 ** 2
    # print("x_0 = " + str(x_0))
    # print("y_0 = " + str(y))
    for i in range(ri_num):
        x_new = int(raiz(x_0, y))
        y = x_new ** 2

        if(len(str(x_new)) < d):
            #print("x_" + str(i + 1) + " = 0" + str(x_new))
            ri_temp = "0.0" + str(x_new)
            ri.append(float(ri_temp))
        else:
            #print("x_" + str(i + 1) + " = " + str(x_new))
            ri_temp = "0." + str(x_new)
            ri.append(float(ri_temp))
        #print("y_"+str(i)+ " = " + str(y))

    return ri

def raiz(x_0, y_0):
    d = len(str(x_0))
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
            ri_num = int(input("Ingrese los cantidad de ri: "))
            x_0 = int(input("Ingrese la semilla: "))
        except ValueError:
            print('Revisa tus inputs')
            continue

        resultado = cuadrados_medios(ri_num, x_0)
        print("Numeros ri:", resultado)
        if input('Otra vez? S/N: ').upper() == 'N': break
    return resultado

if __name__ == '__main__':
    run_lc()
