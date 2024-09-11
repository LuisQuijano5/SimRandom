import cuadrados_medios
import productos_medios
import Constant_multiplier
import Linear_congruential

def mostrar_menu():
    print("Selecciona una opción:")
    print("1: Cuadrados medios")
    print("2: Productos medios")
    print("3: Multiplicador constante")
    print("4: Congruencial lineal")
    print("0: Finalizar el programa")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Escribe el número de la opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        if opcion == 1:
            print("Has seleccionado Cuadrados medios.")
            cuadrados_medios.run_lc()  # Ejecuta la función desde cuadrados_medios.py
        elif opcion == 2:
            print("Has seleccionado Productos medios.")
            productos_medios.run_lc()  # Ejecuta la función desde productos_medios.py
        elif opcion == 3:
            print("Has seleccionado Multiplicador constante.")
            Constant_multiplier.run_cm()  # Ejecuta la función desde multiplicador_constante.py
        elif opcion == 4:
            print("Has seleccionado Congruencial lineal.")
            Linear_congruential.run_lc()  # Ejecuta la función desde congruencial_lineal.py
        elif opcion == 0:
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()
