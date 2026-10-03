from datetime import datetime

# Función para determinar si dos horarios chocan
def horarios_chocan(rango_1:str, rango_2:str) -> bool:
    # Formato de hora
    formato = "%H:%M"

    try:
        # Verificar que los intervalos ingresados cumplan con el formato
        if len(rango_1.split("-")) != 2 or len(rango_2.split("-")) != 2:
            raise ValueError("Formato incorrecto. Debe ser 'HH:MM-HH:MM'") # Arrojar error por formato incorrecto


        # Convertir los rangos de horas a objetos datetime y almacenarlos en tuplas
        r1 = tuple(datetime.strptime(hora, formato) for hora in rango_1.split("-")) # Tupla del rango 1
        r2 = tuple(datetime.strptime(hora, formato) for hora in rango_2.split("-")) # Tupla del rango 2

        # Validar si un rango de horas no comienza y termina a la misma hora, además que no puede terminar antes de empezar
        if r1[0] >= r1[1] or r1[0] >= r1[1]:
            raise ValueError("Un rango no puede comenzar y terminar a la misma hora") # Arrojar error de rangos
        
        # Dada una r, r[0] es la hora de inicio y r[1] la de fin
        # La hora de finalización del rango 2 es después del inicio del rango 1 y el comienzo del primero es ma
        return r1[1] > r2[0] and r1[0] < r2[1] # Retorna True, si chocan. De lo contrario, será False

    # Capturar exceciones
    except ValueError as e:
        print(f"Error: {e}")


    
# Pedir entrada de datos
print("Ingrese dos rangos de horas, siguiendo el formato HH:MM-HH:MM \n\n")
rango_1 = input("Rango 1: ")
rango_2 = input("Rango 2: ")

print() # Salto de línea
print(horarios_chocan(rango_1, rango_2)) # Mostrar si los rangos chocan