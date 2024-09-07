# calculadora.py

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por cero.")
    return x / y

def mostrar_menu():
    print("Calculadora básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        seleccion = input("Selecciona una opción (1/2/3/4/5): ")

        if seleccion == '5':
            print("Saliendo...")
            break

        if seleccion in ['1', '2', '3', '4']:
            try:
                x = float(input("Introduce el primer número: "))
                y = float(input("Introduce el segundo número: "))
            except ValueError:
                print("Por favor, introduce un número válido.")
                continue

            if seleccion == '1':
                resultado = sumar(x, y)
                operacion = "+"
            elif seleccion == '2':
                resultado = restar(x, y)
                operacion = "-"
            elif seleccion == '3':
                resultado = multiplicar(x, y)
                operacion = "*"
            elif seleccion == '4':
                try:
                    resultado = dividir(x, y)
                except ValueError as e:
                    print(e)
                    continue
                operacion = "/"

            print(f"{x} {operacion} {y} = {resultado}")
        else:
            print("Opción no válida. Por favor, selecciona una opción del menú.")

if __name__ == "__main__":
    main()
