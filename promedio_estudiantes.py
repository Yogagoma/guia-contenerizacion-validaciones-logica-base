# Función que calcula el promedio de una lista de notas,
# excluyendo el valor más bajo para obtener un promedio general.
def Promedio(lista_promedios):

    # Verifica que la entrada sea una lista y que todos sus elementos sean números.
    if isinstance(lista_promedios, list) and all(isinstance(x, (int, float)) for x in lista_promedios):

        # Busca el menor valor de la lista.
        mas_bajo = min(lista_promedios)

        # Suma todos los valores y elimina el menor para excluirlo del cálculo.
        suma = sum(lista_promedios) - mas_bajo

        # Divide la suma restante entre la cantidad de elementos menos uno.
        promedio = suma / (len(lista_promedios) - 1)

        # Devuelve el promedio calculado.
        return promedio
    else:
        # Si la entrada no es válida, lanza un error claro.
        raise TypeError("La entrada debe ser una lista de números.")

#mock data
# Se crea una lista con varios promedios y se calcula el promedio general sin el más bajo.
promedio = Promedio([10.23, 20.00, 14.78, 17.83, 13.6])

# Muestra el resultado en pantalla con dos decimales.
print(f"El promedio general sin el más bajo es: {promedio:.2f}")