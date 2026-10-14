# ============================================================
# IMPORTS (modulos que traemos para usar sus herramientas)
# ============================================================

# "csv" es un modulo de la biblioteca estandar de Python (viene incluido,
# no hay que instalar nada). Sirve para leer y escribir archivos CSV
# (tablas en texto plano separadas por comas) sin tener que montar
# las comas y comillas a mano.
import csv

# "os" tambien es de la biblioteca estandar. Sirve para interactuar con el
# sistema operativo: comprobar si un archivo existe, crear carpetas, etc.
import os

# ============================================================
# CONSTANTES (valores fijos que usa el programa)
# ============================================================
# Por convencion se escriben en MAYUSCULAS para indicar "esto no cambia
# mientras el programa corre". Python no lo impide, es solo una norma de estilo.

# Ruta del archivo donde se guardan las series. "datos/" es una carpeta
# relativa a donde ejecutes el script.
ARCHIVO = "datos/entrenos.csv"

# Nombres de las columnas, en el orden en que se escribirán en el CSV.
# Es una lista de textos; la fila de cabecera será exactamente esta lista.
CABECERA = ["fecha", "ejercicio", "serie", "peso_kg", "reps"]


# ============================================================
# FUNCIONES
# ============================================================

def guardar_serie(fecha, ejercicio, serie, peso_kg, reps):
    """Añade UNA serie al final del CSV.

    Si el archivo todavía no existe, lo crea y escribe primero la cabecera.

    Parámetros (los valores que recibe la función):
        fecha     -- texto con la fecha, por ejemplo "2026-10-14"
        ejercicio -- nombre del ejercicio, por ejemplo "press banca"
        serie     -- número de la serie dentro del ejercicio (1, 2, 3...)
        peso_kg   -- peso usado, en kilos (puede tener decimales: 62.5)
        reps      -- repeticiones completadas en esa serie
    """

    # --- Paso 1: asegurar que la carpeta "datos/" existe ---
    # os.path.dirname(ARCHIVO) extrae solo la carpeta de la ruta:
    # de "datos/entrenos.csv" saca "datos".
    # os.makedirs crea esa carpeta. Con exist_ok=True no da error si ya existe.
    # Esto es necesario porque "datos/" está en el .gitignore: si clonas el repo
    # en otro ordenador (o en Docker o GitHub Actions) la carpeta no existirá.
    os.makedirs(os.path.dirname(ARCHIVO), exist_ok=True)

    # --- Paso 2: comprobar si el archivo existía ANTES de abrirlo ---
    # os.path.exists devuelve True o False. Guardamos el resultado en una
    # variable ahora, porque en cuanto abramos el archivo en modo "a" se creará
    # solo y la comprobación dejaría de servir.
    archivo_ya_existia = os.path.exists(ARCHIVO)

    # --- Paso 3: abrir el archivo y escribir ---
    # "with" abre el archivo y garantiza que se cierre solo al terminar el
    # bloque, aunque haya un error por medio.
    #   "a"            -> modo append: escribe al final, sin borrar lo anterior
    #                     (si el archivo no existe, lo crea).
    #   newline=""     -> evita que en Windows aparezcan líneas en blanco entre
    #                     filas (el módulo csv ya gestiona los saltos de línea).
    #   encoding="utf-8" -> codificación de texto estándar, para que las tildes
    #                     y la "ñ" se guarden bien.
    with open(ARCHIVO, "a", newline="", encoding="utf-8") as f:
        # csv.writer envuelve el archivo y sabe escribir filas separadas por comas.
        escritor = csv.writer(f)

        # Solo la primera vez (archivo nuevo) escribimos los nombres de columna.
        if not archivo_ya_existia:
            escritor.writerow(CABECERA)

        # Escribimos la fila con los 5 valores, en el mismo orden que CABECERA.
        escritor.writerow([fecha, ejercicio, serie, peso_kg, reps])


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
# Este bloque solo se ejecuta cuando lanzas el archivo directamente
# (python entreno.py). Si otro archivo hace "import entreno", este bloque NO
# se ejecuta. Así podremos importar guardar_serie en los tests sin que se
# guarde una serie de prueba cada vez.
if __name__ == "__main__":
    # Llamada de prueba con datos escritos a mano.
    guardar_serie("2026-10-14", "press banca", 1, 60, 8)