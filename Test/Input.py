def get_tabular_input():
    data = []
    print("Ingresa los números aleatorios y presiona enter (Sugerencia copia y pega los valores de excel) : ")

    while True:
        line = input()
        if not line:
            break
        for x in line.split():
            try:
                data.append(float(x))
            except ValueError:
                pass

    return data

def get_significance():
    while True:
        a = input("Ingresa la significacia (a): ")
        try:
            a = float(a)
        except ValueError:
            continue
        return a

if __name__ == '__main__':
    get_tabular_input()