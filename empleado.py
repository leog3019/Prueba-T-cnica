class Empleado:

    def __init__(self, nombre, apellido, id_empleado, salarioBase):
        self._nombre = nombre
        self._apellido = apellido
        self._id = id_empleado
        self._salarioBase = salarioBase

    # --- Getters para mostrar informacion 
    def get_nombre_completo(self):
        return f"{self._nombre} {self._apellido}"  
    
    def get_id(self):
        return self._id

    # --- calcular el salario esto se sobreescribe con sus clases hijas
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

    def calcularSalario(self):

        salario_total = self._horasTrabajadas * self._pagoPorHora
        return salario_total

    def mostrarInformacion(self):

        print(f"ID: {self.get_id()}")
        print(f"Nombre: {self.get_nombre_completo()}")
        print(f"Tipo: Por Horas")
        print(f"Detalle: {self._horasTrabajadas} horas * ${self._pagoPorHora:,.2f}/hora")
        print(f"Salario Calculado: ${self.calcularSalario():,.2f}")