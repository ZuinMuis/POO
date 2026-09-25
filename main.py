from paciente import Paciente

pacientes: list[Paciente] = [
    Paciente("11.111.111-1", "Miguel Latos", 50, "Fonasa"),
    Paciente("22.222.222-2", "Luis Arriagada", 40, "Isapre"),
]


def leer_numero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debe ingresar un número.")


def menu() -> int:
    print("\nClínica")
    print("1.- Agregar Paciente")
    print("2.- Editar Paciente")
    print("3.- Eliminar Paciente")
    print("4.- Imprimir Un paciente")
    print("5.- Imprimir Todos los pacientes")
    print("6.- Salir")
    return leer_numero("Seleccione una opción: ")

def agregar_paciente() -> None:
    rut = input("Ingrese el RUT del paciente: ")
    nombre = input("Ingrese el nombre del paciente: ")
    edad = leer_numero("Ingrese la edad del paciente: ")
    print("Previsiones disponibles")
    print("1.-Fonasa")
    print("2.-Isapre")
    print("3.-Particular")
    print("4.-Otro")
    print("5.-Salir")
    Prevision = leer_numero("Seleccione una opción: ")
    if Prevision == 1:
        prevision = "Fonasa"
    elif Prevision == 2:
        prevision = "Isapre"
    elif Prevision == 3:
        prevision = "Particular"
    elif Prevision == 4:
        prevision = "Otro"
    else:
        print("Error: Opción inválida")
        return

    paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")
  


def main():
    while True:
        op = menu()
        if op == 1:
            print("Agregar Paciente")
            agregar_paciente()
        elif op == 2:
            print("Editar Paciente")
        elif op == 3:
            print("Eliminar Paciente")
        elif op == 4:
            print("Imprimir Paciente")
        elif op == 5:
            for p in pacientes:
                print(p)
        elif op == 6:
            print("Saliendo del Programa")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()