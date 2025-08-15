# SE CREA LA CLASE SERIE E I INICIALIZA CON DEF_INIT CON LOS ATRIBUTOS DEFINIDOS PREVIAMENTE

class Serie:
    def __init__(self, titulo, tipo, total_episodios, vistos, puntaje, completada):
        # ATRIBUTOS PRINCIPALES DE LA SERIE
        self.titulo = titulo                # CADENA: NOMBRE DE LA SERIE
        self.tipo = tipo                    # CADENA: "KDRAMA" O "ANIME"
        self.total_episodios = total_episodios  # ENTERO: TOTAL DE EPISODIOS
        self.vistos = vistos                # ENTERO: EPISODIOS VISTOS
        self.puntaje = puntaje              # FLOTANTE: PUNTAJE DEL 0 AL 10
        self.completada = completada        # BOOLEANO: SI LA SERIE ESTÁ COMPLETADA

    def __str__(self):  # STR SE USA PARA DEVOLVER EL OBJETO EN FORMATO DE CADENA
        # ESTADO SE USA PARA MOSTRAR SI LA SERIE ESTÁ COMPLETADA
        estado = "Sí" if self.completada else "No"
        return (f"Título: {self.titulo} | Tipo: {self.tipo} | "
                f"Episodios: {self.vistos}/{self.total_episodios} | "
                f"Puntaje: {self.puntaje} | Completada: {estado}")

    def to_line(self):  # TO LINE SE USA PARA CONVERTIR LOS DATOS DE LA SERIE EN UNA LÍNEA DE TEXTO Y GUARDAR EN EL ARCHIVO DE PERSISTENCIA DE DATOS
        # LOS CAMPOS SE SEPARAN POR PIPE "|" PARA FACILITAR EL PARSEO O LA LECTURA
        return f"{self.titulo}|{self.tipo}|{self.total_episodios}|{self.vistos}|{self.puntaje}|{self.completada}"

    # METODO ESTATICO PARA CONVERTIR UNA LÍNEA DE TEXTO EN UN OBJETO SERIE (STATICMETHOD PORQUE NO DEPENDE DE UNA INSTANCIA)
    @staticmethod
    def from_line(linea):
        # EL ATRIBUTO PARTES SE USA PARA ALMACENAR LOS VALORES SEPARADOS POR PIPE Y QUITANDO ESPACIOS VACIOS
        partes = linea.strip().split("|")
        titulo = partes[0]
        tipo = partes[1]
        total_episodios = int(partes[2])
        vistos = int(partes[3])
        puntaje = float(partes[4])
        # EL ATRIBUTO COMPLETADA SE USA PARA CONVERTIR CADENA A BOOLEANO
        completada = partes[5] == "True"
        return Serie(titulo, tipo, total_episodios, vistos, puntaje, completada)
