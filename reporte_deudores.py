# Equipo 3: Reto 3

# mock data
estudiantes = [
    {'nombre': 'Lionel Messi', 'estado': 'Solvente'},
    {'nombre': 'Cristiano Ronaldo', 'estado': 'Deudor'},
    {'nombre': 'Camila Navarro', 'estado': 'Deudor'},
    {'nombre': 'Valeria Fernadez', 'estado': 'Deudor'},
    {'nombre': 'Gabriel Delgado', 'estado': 'Deudor'},
]


# Funcion encargada de formatear la salida de Alumnos Deudores
# Estudiantes es la lista con todos los estudiantes, estos se alamacenan en un diccionario que tiene las llaves nombre y estado, si se desea se le pueden agregar mas llaces como su promedio, la carrera que esta cursando o el semestre que estan cursando, pero en este caso solo alamecnaremos el nombre y el estado.
def generarReporteDeudores(estudiantes: list): 
    # A traves de la programacion funcional con el uso de filter y lambda obtenemos los los estudiantes que se estado es "Deudor"  y descartamos los estudiantes que no tiene este estado ("Solvente")
    alumnos_deudores =  filter(lambda item : item['estado'] == 'Deudor', estudiantes)

    # Se convierte el filter_object en una lista que podremos iterar y manipular
    alumnos_deudores_listados = list(alumnos_deudores)

    # Se verifica si la lista esta vacia o no, en caso de estar vacia(todos los estudiantes estan solventes) imprime un mensaje indicando que los estudiantes estan solventes.
    # En caso contrario, imprime la lista de deudores formateada.
    if alumnos_deudores_listados:
        print("#"*40) # Imprime el caracter "#" 40 veces para dar el efecto de linea divisora
        print("LISTA DEUDORES".center(40))
        print("#"*40, end="\n\n") # Imprime el caracter "#" 40 veces para dar el efecto de linea divisora y esta impresion finaliza con dos saltos de linea en lugar de uno solo.
        print(" NOMBRE                  ESTADO") 
        
        # Se recorre todos los alumnos que se encuentran en la lista de deudores y se imprimen
        for alumno in alumnos_deudores_listados:
            print("-"*40) # Imprime el caracter "-" 40 veces para dar el efecto de linea divisora
            print(f" {alumno['nombre']:<20}         {alumno['estado']}") #Se imprime el nombre del alumno y el estado, en el nombre :<20 alinea el nombre a la izquierda y rellana con espacios en blanco hasta llegar a ocupar 20 espacios.
        print("#"*40) # Imprime el caracter "#" 40 veces para dar el efecto de linea divisora
    else:
        # Mensaje que se muestra cuando no hay estudiantes deudores.
        print('#'*40)
        print('')
        print("   TODOS LOS ALUMNOS ESTAN SOLVENTES")
        print("")
        print('#'*40)
       

generarReporteDeudores(estudiantes) # Se llama a la funcion y se le pasan los datos de prueba o mock data