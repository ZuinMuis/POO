import sqlite3 
from sqlite3 import Connection, Cursor

class Database:
    """
    Clase que representa una base de datos SQLite y proporciona métodos para interactuar con ella.
    """
    _instance = None
    _db_path = "database.db"


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connection = sqlite3.connect(cls._db_path)
            cls._instance._cursor = cls._instance._connection.cursor()
        return cls._instance

    def get_connection(self) -> Connection:
        """
        Devuelve la conexión a la base de datos.
        """
        conn =sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row # Esto permite acceder a las filas como diccionarios, lo que facilita la lectura de los datos.
        return conn

    def init_db(self ) -> None:
        """
        Inicializa la base de datos creando las tablas necesarias.
        """
        conn = self.get_connection()
        try:    
            cursor = conn.cursor()

            # Crear tabla de departamentos
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS departamet  (
                    id_department INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    piso INTEGER NOT NULL
                )
            ''')

            # Crear tabla pacientes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pacientes (
                    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL,
                    prevision TEXT NOT NULL,
                    id_department INTEGER NOT NULL,
                    FOREIGN KEY (id_department) REFERENCES departamet(id_department) ON DELETE SET NULL
                )
            ''')

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error al inicializar la base de datos: {e}")    
        finally:
            conn.close()
        
if __name__ == "__main__":
    db = Database()
    db.init_db()
    print("Base de datos inicializada correctamente.")


