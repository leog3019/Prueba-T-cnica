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

class EmpleadoTiempoCompleto(Empleado):

    def __init__(self, nombre, apellido, id_empleado, salarioBase):
        super().__init__(nombre, apellido, id_empleado, salarioBase)
        self._bono = 0.10 # 10%

    def calcularSalario(self):
        salario_base = super().calcularSalario()
        salario_total = salario_base + (salario_base * self._bono)
        return salario_total

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Tipo: Tiempo Completo")
        print(f"Salario Calculado (con bono): ${self.calcularSalario():,.2f}")


class EmpleadoPorHoras(Empleado):

    def __init__(self, nombre, apellido, id_empleado, horasTrabajadas, pagoPorHora):
        super().__init__(nombre, apellido, id_empleado, 0) 
        self._horasTrabajadas = horasTrabajadas
        self._pagoPorHora = pagoPorHora
