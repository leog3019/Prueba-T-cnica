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