from empleado import Empleado, EmpleadoTiempoCompleto, EmpleadoPorHoras

def ejecutar_nomina():
    
    emp_completo = EmpleadoTiempoCompleto("Ana", "García", "001", 3000)
    emp_horas = EmpleadoPorHoras("Juan", "Pérez", "002", 40, 15)
    empleados = [emp_completo, emp_horas]
    
    print("--- INFORME DE NÓMINA DATHA+ ---")
    
    for empleado in empleados:
        empleado.mostrarInformacion()
        print("-" * 50)

if __name__ == "__main__":
    ejecutar_nomina()