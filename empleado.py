class Empleado:

    def __init__(self, nombre, apellido, id_empleado, salarioBase):
        #encapsulamiento
        self._apellido = apellido
        self._id = id_empleado
        self._salarioBase = salarioBase

    # Getters
    def get_nombre_completo(self):
        return f"{self._nombre} {self._apellido}"
    
    def get_id(self):
        return self._id

    def calcularSalario(self):
        return self._salarioBase

    def mostrarInformacion(self):
        print(f"ID: {self._id}")
        print(f"Nombre: {self.get_nombre_completo()}")
        print(f"Salario Base: ${self._salarioBase:,.2f}")
