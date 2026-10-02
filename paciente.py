class Paciente:
    
    PREVISIONES: set[str] = {"Fonasa", "Isapre", "Particular", "Otro"}



    def __init__(self, rut: str, nombre: str, edad: int, prevision: str) -> None:
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision

    @property
    def rut(self) -> str:
        return self._rut

    @rut.setter
    def rut(self, rut: str) -> None:
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("RUT inválido.")
        self._rut = rut.strip().upper()
        

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        if not isinstance(nombre, str) or len(nombre.strip()) < 3:
            raise ValueError("Nombre inválido debe de ser de 3 caracteres como mínimo.")
        self._nombre = nombre.strip().upper()

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, edad: int) -> None:
        if not isinstance(edad, int):
            raise TypeError("la edad debe ser un numero entero.")
        if edad < 0 or edad > 125:
            raise ValueError("Edad inválida, debe estar entre 0 y 125.")
        self._edad = edad
    
    

    @property
    def prevision(self) -> str:
        return self._prevision

    @prevision.setter
    def prevision(self, prevision: str) -> None:
        if not isinstance(prevision,str):
            raise TypeError("La previsión debe ser una cadena de texto.")
        prevision = prevision.strip().capitalize()
        if prevision not in self.PREVISIONES:
            raise ValueError(f"Previsión inválida. Debe ser una de las siguientes: {', '.join(self.PREVISIONES)}.")
        self._prevision = prevision
        


    def __str__(self) -> str:
        return f"Informacion del paciente:\nRUT: {self.rut}\nNombre: {self.nombre}\nEdad: {self.edad}\nPrevision: {self.prevision}"

    def __repr__(self) -> str:
        return f"Paciente(rut='{self.rut}', nombre='{self.nombre}', edad={self.edad}, prevision='{self.prevision}')"