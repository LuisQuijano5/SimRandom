from Generate import Constant_multiplier, productos_medios, Linear_congruential, cuadrados_medios
from Variance import run_variance
from Independence import run_independence
from Uniformity import run_uniformity
from Avarage import run_avarage

generate_options = ["Cuadrados medios", "Productos medios", "Multiplicador constante", "Congurencial lineal"]
generate_menu = {1: cuadrados_medios.run_lc,
                 2: productos_medios.run_lc,
                 3: Constant_multiplier.run_cm,
                 4: Linear_congruential.run_lc}

tests_options = ["Medias", "Varianza", "Uniformidad", "Independencia"]
tests_menu = {1: run_avarage,
              2: run_variance,
              3: run_uniformity,
              4: run_independence}


def mostrar_menu(options, main):
    print("\nSelecciona una opción:")
    for i, x in enumerate(options):
        print(str(i + 1) + ":", x)
    print("0: Terminar" if main else "0: Regresar")


def user_input(menu, main):
    mostrar_menu(menu, main)
    try:
        opcion = int(input("Escribe el número de la opción: "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        return False
    return opcion


def run_generate():
    options = generate_options
    menu = generate_menu
    selection = user_input(options, False)
    if selection == 0:
        return
    last_values = menu[selection]()
    print(last_values)
    if input('Quiere probar los últimos números ri generados? Y/N: ').upper() == 'Y':
        test_selection = user_input(tests_options, False)
        tests_menu[test_selection](last_values)


def run_tests():
    options = tests_options
    menu = tests_menu
    selection = user_input(options, False)
    if selection == 0:
        return
    menu[selection](None)


main_options = ["Generación números ri", "Pruebas de números ri"]
main_menu = {1: run_generate, 2: run_tests}

all_options = {0: (main_options, main_menu), 1: (generate_options, generate_menu), 2: (tests_options, tests_menu)}


def run(menu_index):
    options, menu = all_options[menu_index]
    selection = -1
    while selection != 0:
        selection = user_input(options, True)

        if not selection:
            continue
        if selection == 0:
            continue

        print("\n\nSeleccionaste:", options[selection - 1])
        menu[selection]()



if __name__ == "__main__":
    run(0)
