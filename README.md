🎬 AnimesKdramasManager - Gestor de Series Anime y Kdramas 🎭

¿Para qué sirve este proyecto?
- Este programa permite gestionar series de anime y kdramas, almacenándolas en listas separadas.  
- Facilita agregar, mostrar y guardar series en archivos `.txt` para persistencia de datos.  
- Usa un menú interactivo para facilitar la experiencia del usuario.

Python y Programación Orientada a Objetos (POO)
- Manejo de variables, tipos (str, int, float, bool), condicionales y bucles para controlar el flujo.
- Uso de clases para encapsular datos y funcionalidades, modularización, manejo de archivos y persistencia de datos mediante listas y archivos .txt. 
- Manejo de errores con bloques try-except para evitar fallos en la lectura o escritura de archivos.

Mejoras futuras
- Uso de herencia y polimorfismo para diferenciar clases Anime y Kdrama, y permitir métodos personalizados para cada tipo.
- Implementación de setters y getters para controlar y validar el acceso a los atributos de las series, mejorando la encapsulación.

AnimesKdramasManager/
│
├── main.py           # Menú principal e interfaz con el usuario  
├── gestor_series.py  # Clase GestorSeries para manejo de datos y archivos  
├── serie.py          # Clase Serie que representa cada serie  
├── anime.txt         # Archivo que guarda la lista de animes  
└── kdrama.txt        # Archivo que guarda la lista de kdramas