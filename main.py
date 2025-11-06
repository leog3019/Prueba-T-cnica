from empleado import Empleado, EmpleadoTiempoCompleto, EmpleadoPorHoras #improtamos las clases desde empleado.py


#definimos esta funcion para hacer la prueba de la nomina

def ejecutar_nomina():
    
    emp_completo = EmpleadoTiempoCompleto("Ana", "García", "001", 3000)
    emp_horas = EmpleadoPorHoras("Juan", "Pérez", "002", 40, 15)
    empleados = [emp_completo, emp_horas] # lista de empleados
    
    print("--- INFORME DE NÓMINA DATHA+ ---")
    
    #recorre toda la lista de empleados para mostrar su informacion y su salario calculado
    for empleado in empleados:
        empleado.mostrarInformacion()
        print("-" * 50)

if __name__ == "__main__":
    ejecutar_nomina() # ejecuta la funcion para mostrar la nomina