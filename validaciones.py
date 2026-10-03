import re
    #Equipo 2 (Académico y Calificaciones)
def validar_modulo_academico(nota: str, codigo_materia: str, observacion: str) -> dict:
    # 1. Validación de nota (0 a 20, con opcional de 1 a 2 decimales)
    # Permite: "15", "09.5", "20", "20.00". Rechaza: "25", "-2", "20.1", letras.
    regex_nota = r'^(?:1?[0-9](?:\.[0-9]{1,2})?|20(?:\.0{1,2})?)$'
    nota_valida = bool(re.match(regex_nota, str(nota)))

    # 2. Validación de código de asignatura (Ejemplo: MAT-101, FIS-202)
    # 3 letras mayúsculas, un guion, y 3 números.
    regex_codigo = r'^[A-Z]{3}-\d{3}$'
    codigo_valido = bool(re.match(regex_codigo, codigo_materia))

    # 3. Sanitización básica contra XSS en las observaciones del docente
    observacion_segura = re.sub(r'<[^>]*>', '', observacion)

    return {
        "nota_valida": nota_valida,
        "codigo_valido": codigo_valido,
        "observacion_sanitizada": observacion_segura
    }

# Prueba (Mock data)
resultado = validar_modulo_academico(
    nota="19.50",
    codigo_materia="MAT-101",
    observacion="<script>alert('XSS')</script>Excelente desempeño en el lapso."
)
