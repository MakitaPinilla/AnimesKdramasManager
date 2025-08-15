# SE IMPORTAN LOS MODULOS SERIE Y GESTOR SERIES PARA PODER CORRER EL PROGRAMA PRINCIPAL : MAIN
from serie import Serie
from gestor_series import GestorSeries

# INICIALIZAMOS EL GESTOR Y CARGAMOS LAS SERIES DE LOS ARCHIVOS
gestor = GestorSeries()  # ESTO INICIALIZA EL GESTOR DE SERIES
# ESTO CARGA LAS SERIES DESDE LOS ARCHIVOS, SI ESTUVIERA VACÍO SE CREARÍAN NUEVOS ARCHIVOS
gestor.cargar_desde_archivo()

# FUNCIÓN PARA MOSTRAR EL MENÚ PRINCIPAL Y MANEJAR LAS OPCIONES DEL USUARIO


def menu():
    # MENÚ PRINCIPAL DEL PROGRAMA
    print("\n BIENVENIDO A NIBUSAN ")
    print("1. AGREGAR KDRAMA")
    print("2. AGREGAR ANIME")
    print("3. VER LISTA DE KDRAMAS")
    print("4. VER LISTA DE ANIMES")
    print("5. BUSCAR SERIE")
    print("6. ELIMINAR SERIE")
    print("7. GUARDAR Y SALIR")


# CICLO PRINCIPAL: SE USA WHILE PARA CUMPLIR UNA CONDICION O HASTA QUE EL USUARIO DECIDA SALIR (BREAK)
while True:
    menu()
    opcion = input("SELECCIONA UNA OPCIÓN (1-7): ")

    if opcion == "1" or opcion == "2":
        # SELECCIONAR TIPO DE SERIE SEGÚN OPCIÓN
        tipo = "KDRAMA" if opcion == "1" else "ANIME"
        print(f"\n AGREGANDO NUEVO {tipo}")

        titulo = input("TÍTULO DE LA SERIE: ")
        try:
            total = int(input("EPISODIOS TOTALES: "))
            vistos = int(input("EPISODIOS VISTOS: "))
            puntaje = float(input("PUNTAJE (0-10): "))
            completada = input("¿COMPLETADA? (s/n): ").lower() == "s"

            nueva_serie = Serie(titulo, tipo, total,
                                vistos, puntaje, completada)
            gestor.agregar_serie(nueva_serie)
            print(f" {tipo} AGREGADO CON ÉXITO.")
        except ValueError:
            print(" DATOS INVÁLIDOS. INTÉNTALO DE NUEVO.")

    elif opcion == "3":
        # MOSTRAR SOLO KDRAMAS
        gestor.mostrar_series("KDRAMA")

    elif opcion == "4":
        # MOSTRAR SOLO ANIMES
        gestor.mostrar_series("ANIME")

    elif opcion == "5":
        # BUSCAR SERIE POR TÍTULO
        titulo = input("TÍTULO A BUSCAR: ")
        serie = gestor.buscar_serie(titulo)
        if serie:
            print(" SERIE ENCONTRADA:")
            print(serie)
        else:
            print(" SERIE NO ENCONTRADA.")

    elif opcion == "6":
        # ELIMINAR SERIE POR TÍTULO
        titulo = input("TÍTULO A ELIMINAR: ")
        if gestor.eliminar_serie(titulo):
            print(" SERIE ELIMINADA.")
        else:
            print(" SERIE NO ENCONTRADA.")

    elif opcion == "7":
        # GUARDAR Y SALIR DEL PROGRAMA
        gestor.guardar_en_archivo()
        print(" SERIES GUARDADAS. ¡HASTA PRONTO!")
        break

    else:
        print(" OPCIÓN NO VÁLIDA. INTENTA DE NUEVO.")
