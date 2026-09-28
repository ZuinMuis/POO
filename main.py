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
            print("Error: Debe ingresar un número válido.")


def menu() -> int:
    print("\n--- Menú Clínica ---")
    print("1.- Agregar Paciente")
    print("2.- Editar Paciente")
    print("3.- Eliminar Paciente")
    print("4.- Imprimir Un paciente")
    print("5.- Imprimir Todos los pacientes")
    print("6.- Salir")
    return leer_numero("Seleccione una opción: ")


def buscar_paciente() -> Paciente | None:
    rut = input("Ingrese RUT del paciente: ").strip()
    for paciente in pacientes:
        if paciente.rut == rut:
            return paciente
    return None


def seleccionar_prevision() -> str | None:
    print("\nPrevisiones disponibles:")
    
    print("1.- Fonasa")
    print("2.- Isapre")
    print("3.- Particular")
    print("4.- Otro")
    
    opcion = leer_numero("Seleccione una opción: ")
    previsiones = {1: "Fonasa", 2: "Isapre", 3: "Particular", 4: "Otro"}
    
    return previsiones.get(opcion, None)


def agregar_paciente() -> None:
    print("\n--- Agregar Paciente ---")
    rut = input("Ingrese el RUT del paciente: ").strip()
    
    # Validar que el RUT no esté duplicado
    for p in pacientes:
        if p.rut == rut:
            print("Error: Ya existe un paciente registrado con ese RUT.")
            return

    nombre = input("Ingrese el nombre del paciente: ").strip()
    
    while True:
        edad = leer_numero("Ingrese la edad del paciente: ")
        if edad >= 0:
            break
        print("Error: La edad debe ser mayor o igual a 0.")

    prevision = seleccionar_prevision()
    if not prevision:
        print("Error: Opción de previsión inválida.")
        return

    paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")


def editar_paciente() -> None:
    print("\n--- Editar Paciente ---")
    paciente = buscar_paciente()
    if not paciente:
        print("Error: Paciente no encontrado.")
        return

    print(f"\nEditando a: {paciente.nombre} (RUT: {paciente.rut})")
    nuevo_nombre = input("Ingrese nuevo nombre (dejar en blanco para conservar el actual): ").strip()
    if nuevo_nombre:
        paciente.nombre = nuevo_nombre

    nueva_edad_str = input("Ingrese nueva edad (dejar en blanco para conservar la actual): ").strip()
    if nueva_edad_str:
        try:
            nueva_edad = int(nueva_edad_str)
            if nueva_edad >= 0:
                paciente.edad = nueva_edad
            else:
                print("Edad inválida, se conservó la anterior.")
        except ValueError:
            print("Valor no numérico, se conservó la edad anterior.")

    cambiar_prev = input("¿Desea cambiar la previsión? (s/n): ").strip().lower()
    if cambiar_prev == 's':
        nueva_prevision = seleccionar_prevision()
        if nueva_prevision:
            paciente.prevision = nueva_prevision

    print("Paciente actualizado con éxito.")


def imprimir_un_paciente() -> None:
    print("\n--- Imprimir Un Paciente ---")
    paciente = buscar_paciente()
    if paciente:
        print("\nInformación del paciente:")
        print(paciente)
    else:
        print("Error: Paciente no encontrado.")


def imprimir_todos_los_pacientes() -> None:
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    for i, p in enumerate(pacientes, start=1):
        print(f"{i}. {p}")


def eliminar_paciente() -> None:
    print("\n--- Eliminar Paciente ---")
    paciente = buscar_paciente()
    if paciente:
        confirmacion = input(f"¿Está seguro de que desea eliminar a {paciente.nombre}? (s/n): ").strip().lower()
        if confirmacion == 's':
            pacientes.remove(paciente)
            print("Paciente eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print("Error: Paciente no encontrado.")

def editar_paciente() -> None:
    print("\n--- Editar Paciente ---")
    paciente = buscar_paciente()
    if paciente:
        nuevo_nombre = input("Ingrese nuevo nombre (dejar en blanco para conservar el actual): ").strip()
        if nuevo_nombre:
            paciente.nombre = nuevo_nombre

        nueva_edad_str = input("Ingrese nueva edad (dejar en blanco para conservar la actual): ").strip()
        if nueva_edad_str:
            try:
                nueva_edad = int(nueva_edad_str)
                if nueva_edad >= 0:
                    paciente.edad = nueva_edad
                else:
                    print("Edad inválida, se conservó la anterior.")
            except ValueError:
                print("Valor no numérico, se conservó la edad anterior.")

        cambiar_prev = input("¿Desea cambiar la previsión? (s/n): ").strip().lower()
        if cambiar_prev == 's':
            nueva_prevision = seleccionar_prevision()
            if nueva_prevision:
                paciente.prevision = nueva_prevision

        print("Paciente actualizado con éxito.")


def main():
    while True:
        op = menu()
        if op == 1:
            agregar_paciente()
        elif op == 2:
            editar_paciente()
        elif op == 3:
            eliminar_paciente()
        elif op == 4:
            imprimir_un_paciente()
        elif op == 5:
            imprimir_todos_los_pacientes()
        elif op == 6:
            print("Saliendo del Programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()