# la estructura basica del programa es crear el empleado basico y de ahi crear las clases hijas que heredan de empleado 
# cada clase hija tiene su propia forma de calcular el salario y mostrar la informacion
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

    # --- calcular el salario esto se sobreescribe con sus clases hijas donde se calcular el salario con bono o por horas
    def calcularSalario(self):
            return self._salarioBase

    def mostrarInformacion(self): # Muestra la información básica del empleado
        print(f"ID: {self._id}")
        print(f"Nombre: {self.get_nombre_completo()}")
        print(f"Salario Base: ${self._salarioBase:,.2f}")

class EmpleadoTiempoCompleto(Empleado):

    def __init__(self, nombre, apellido, id_empleado, salarioBase):
        super().__init__(nombre, apellido, id_empleado, salarioBase) #llamamos al contructos base de empleado para inicializar los atributos comunes
        self._bono = 0.10 # 10% bono

    def calcularSalario(self):
        salario_base = super().calcularSalario()
        salario_total = salario_base + (salario_base * self._bono)
        return salario_total

    def mostrarInformacion(self):

        super().mostrarInformacion() # usamos super para llamar al metodo de la clase base 
        print(f"Tipo: Tiempo Completo")
        print(f"Salario Calculado (con bono): ${self.calcularSalario():,.2f}")


class EmpleadoPorHoras(Empleado):

    def __init__(self, nombre, apellido, id_empleado, horasTrabajadas, pagoPorHora):
        super().__init__(nombre, apellido, id_empleado, 0) # el numero de horas no afecta el salario base por lo que inicializamos con 0
        self._horasTrabajadas = horasTrabajadas
        self._pagoPorHora = pagoPorHora

    def calcularSalario(self):

        salario_total = self._horasTrabajadas * self._pagoPorHora 
        return salario_total

    def mostrarInformacion(self):

        #usamos los getters para obtener la informacion del empleado ya que la clase base no tiene salario base por lo que no podemos usar super()
        print(f"ID: {self.get_id()}")
        print(f"Nombre: {self.get_nombre_completo()}")
        print(f"Tipo: Por Horas")
        print(f"Detalle: {self._horasTrabajadas} horas * ${self._pagoPorHora:,.2f}/hora")
        print(f"Salario Calculado: ${self.calcularSalario():,.2f}")