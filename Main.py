from Generate import Constant_multiplier, productos_medios, Linear_congruential, cuadrados_medios

generate_options = ["Cuadrados medios", "Productos medios", "Multiplicador constante", "Congurencial lineal"]
generate_menu = {1: cuadrados_medios.run_lc,
                 2: productos_medios.run_lc,
                 3: Constant_multiplier.run_cm,
                 4: Linear_congruential.run_lc}

tests_options = ["Medias", "Varianza", "Uniformidad", "Independencia"]
tests_menu = {1: cuadrados_medios.run_lc,
              2: productos_medios.run_lc,
              3: Constant_multiplier.run_cm,
              4: Linear_congruential.run_lc}

main_options = ["Generación números ri", "Pruebas de números ri"]
main_menu = {1: lambda: run(1), 2: lambda: run(2)}

all_options = {0: (main_options, main_menu), 1: (generate_options, generate_menu), 2: (tests_options, tests_menu)}


def mostrar_menu(options):
    print("Selecciona una opción:")
    for i, x in enumerate(options):
        print(str(i + 1) + ":", x)
    print("0: Terminar" if options[0] == main_options[1] else "0: Regresar")


def user_input(menu):
    mostrar_menu(menu)
    try:
        opcion = int(input("Escribe el número de la opción: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return False
    return opcion


def run(menu_index):
    options, menu = all_options[menu_index]
    while True:
        selection = user_input(options)

        if not selection:
            continue
        elif selection == 0:
            break

        print("Seleccionaste:", options[selection])
        menu[selection]()


if __name__ == "__main__":
    run(0)
