# IMPORTAMOS OS PARA USAR OS.PATH.EXISTS Y VERIFICAR SI LOS ARCHIVOS EXISTEN ANTES DE LEERLOS
import os
from serie import Serie

# CLASE PRINCIPAL PARA GESTIONAR LAS SERIES


class GestorSeries:
    def __init__(self):
        # INICIALIZAMOS DOS LISTAS SEPARADAS PARA KDRAMAS Y ANIMES
        self.kdramas = []
        self.animes = []

# METODO PARA CARGAR SERIES DESDE ARCHIVO, USA PATH.EXISTS PARA VERIFICAR SI EL ARCHIVO EXISTE
    def cargar_desde_archivo(self):
        # CARGAR KDRAMAS DESDE EL ARCHIVO "kdrama.txt"
        self.kdramas = []
        if os.path.exists("kdrama.txt"):
            # R ES PARA LEER Y ENCODING ES PARA LA CODIFICACIÓN
            with open("kdrama.txt", "r", encoding="utf-8") as f:
                for linea in f:  # FOR ITERA SOBRE CADA LÍNEA DEL ARCHIVO
                    serie = Serie.from_line(linea)
                    if serie.tipo == "KDRAMA":
                        # CON APPEND AGREGAMOS LA SERIE A LA LISTA
                        self.kdramas.append(serie)

        # CARGAR ANIMES DESDE EL ARCHIVO "anime.txt"
        self.animes = []
        if os.path.exists("anime.txt"):
            with open("anime.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    serie = Serie.from_line(linea)
                    if serie.tipo == "ANIME":
                        self.animes.append(serie)

# METODO PARA GUARDAR LAS SERIES EN ARCHIVOS
    def guardar_en_archivo(self):
        # GUARDAR KDRAMAS EN EL ARCHIVO "kdrama.txt"
        with open("kdrama.txt", "w", encoding="utf-8") as f:  # W ES PARA ESCRIBIR
            for serie in self.kdramas:
                # F.WRITE ES PARA ESCRIBIR EN EL ARCHIVO
                f.write(serie.to_line() + "\n")

        # GUARDAR ANIMES EN EL ARCHIVO "anime.txt"
        with open("anime.txt", "w", encoding="utf-8") as f:
            for serie in self.animes:
                f.write(serie.to_line() + "\n")

# METODOS PARA AGREGAR SERIES
    def agregar_serie(self, serie):
        # AGREGAR UNA NUEVA SERIE A LA LISTA CORRESPONDIENTE SEGÚN SU TIPO
        if serie.tipo == "KDRAMA":
            self.kdramas.append(serie)
        elif serie.tipo == "ANIME":
            self.animes.append(serie)

# METODO PARA MOSTRAR SERIES
    def mostrar_series(self, tipo=None):
        # MOSTRAR SERIES, FILTRANDO POR TIPO SI SE PROPORCIONA ("KDRAMA" O "ANIME")
        if tipo == "KDRAMA":
            print("\n=== LISTA DE KDRAMAS ===")
            if not self.kdramas:
                print("NO HAY KDRAMAS REGISTRADOS.")
            else:
                for idx, serie in enumerate(self.kdramas, 1):
                    print(f"{idx}. {serie}")
        elif tipo == "ANIME":
            print("\n=== LISTA DE ANIMES ===")
            if not self.animes:
                print("NO HAY ANIMES REGISTRADOS.")
            else:
                for idx, serie in enumerate(self.animes, 1):
                    print(f"{idx}. {serie}")
        else:
            # SI NO SE ESPECIFICA TIPO, MOSTRAR AMBOS
            self.mostrar_series("KDRAMA")
            self.mostrar_series("ANIME")

# METODO PARA BUSCAR SERIES
    def buscar_serie(self, titulo):
        # BUSCAR SERIE POR TÍTULO EN AMBAS LISTAS
        for serie in self.kdramas + self.animes:
            if serie.titulo.lower() == titulo.lower():
                return serie
        return None

# METODO PARA ELIMINAR SERIES
    def eliminar_serie(self, titulo):
        # ELIMINAR SERIE POR TÍTULO DE AMBAS LISTAS
        for lista in [self.kdramas, self.animes]:
            for serie in lista:
                if serie.titulo.lower() == titulo.lower():
                    lista.remove(serie)
                    return True
        return False
