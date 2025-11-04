import sqlite3

# Define el nombre de tu archivo de base de datos
DATABASE_NAME = 'alquileres.db'


def get_db_connection():
    """
    Crea y retorna una conexión a la base de datos SQLite.
    La conexión usará sqlite3.Row para devolver filas que actúan como diccionarios.
    """
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def init_db():
    """
    Inicializa la base de datos creando las tablas definidas en schema.sql.
    Este script se corre una sola vez (o cada vez que quieras reiniciar la BD).
    """
    conn = get_db_connection()
    if conn is None:
        print("Error: No se pudo crear la conexión a la base de datos.")
        return

    try:
        # Lee el archivo schema.sql
        with open('schema.sql', 'r') as f:
            sql_script = f.read()

        # Ejecuta el script SQL para crear las tablas
        conn.executescript(sql_script)
        conn.commit()
        print("Base de datos inicializada exitosamente.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'schema.sql'.")
    except sqlite3.Error as e:
        print(f"Error al ejecutar el script SQL: {e}")
    finally:
        conn.close()