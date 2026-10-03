import html
import re

#necesito que para mañana implementar que sean ingresados por el usuario:

def validar_correo (email: str) -> bool:
    correo_patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$" #pantron del correo estandar
    coincidencia_correo = re.match(correo_patron,email.strip()) #verifica que el patron se cumpla
    return bool(coincidencia_correo) #retorna el resultado true o false

def validar_telefono(telefono: str)-> bool:
    
    telefono_patron = r"^(\+58|0)(412|414|424|416|426)\d{7}$" #el patron permite colocarlo con guiones o sin guiones
    modificador_telefono = re.sub(r"[^\d+]", "",telefono.strip()) # aqui solo tomara los valores numericos y el + y elimina los espacios o guiones
    coincidencia_telefono = re.match(telefono_patron,modificador_telefono)# se encarga de verificar ya con la con los digitos necesario para su verificacion si lo ingrese cumple con la expresion regular
    return bool(coincidencia_telefono)#retorna el resultado correcto true o false
    
def validar_Cedula(Cedula: str)-> bool:
    Cedula_patron = r"^[VEJ]?-?[0-9]{6,8}$|^[0-9]{6,8}$"#la expresion regular para verificar la cedula
    coincidencia_Cedula = re.match(Cedula_patron,Cedula.strip().upper())#la funcion re.macht se encargar de verificar que coinicida desde el inicio
    return bool(coincidencia_Cedula)#retorna el resultado correcto true o false
    
def sanatizacion_XSS(entrada: str) -> str:# y aqui se limpia, filtra o se transformar los datos que introduce un usuario antes de mostralos en la consola o pagina web
    #Escapa caracteres especiales HTML (<, >, &, ", ') para prevenir ejecución de scripts, es decir transforma eso caracter para que ese texto no sea ejecutable 
    return html.escape(entrada.strip())

#Prueba de las funciones 
if __name__ == "__main__":

    print("\n--- INGRESO DE DATOS POR EL USUARIO ---")
    correo_usuario = input("Ingrese un correo a validar: ")
    print(f"¿Correo válido?: {validar_correo(correo_usuario)}")

    telefono_usuario = input("Ingrese un número telefónico a validar: ")
    print(f"¿Teléfono válido?: {validar_telefono(telefono_usuario)}")

    cedula_usuario = input("Ingrese una Cédula a validar: ")
    print(f"¿Cédula válida?: {validar_Cedula(cedula_usuario)}")

    texto_xss_usuario = input("Ingrese un texto para probar sanitización XSS: ")
    print(f"Resultado sanitizado: {sanatizacion_XSS(texto_xss_usuario)}")