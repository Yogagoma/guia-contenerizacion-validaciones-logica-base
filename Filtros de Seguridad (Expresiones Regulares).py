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
    coincidencia_Cedula = re.match(Cedula_patron,Cedula.strip())#la funcion re.macht se encargar de verificar que coinicida desde el inicio
    return bool(coincidencia_Cedula)#retorna el resultado correcto true o false
    
def sanatizacion_XSS(entrada: str) -> str:# y aqui se limpia, filtra o se transformar los datos que introduce un usuario antes de mostralos en la consola o pagina web
    #Escapa caracteres especiales HTML (<, >, &, ", ') para prevenir ejecución de scripts, es decir transforma eso caracter para que ese texto no sea ejecutable 
    return html.escape(entrada.strip())

#Prueba de las funciones 
if __name__ == "__main__":
    print("Email:", validar_correo("usuario@dominio.com"))  # True
    print("Teléfono:", validar_telefono("0414-1234567"))  # True
    print("Cédula:", validar_Cedula("V-20123456"))  # True
    print(
        "XSS Sanitizado:",
        sanatizacion_XSS("<script>alert('Ataque XSS')</script>"),
    )
    # Output: &lt;script&gt;alert(&#x27;Ataque XSS&#x27;)&lt;/script&gt;