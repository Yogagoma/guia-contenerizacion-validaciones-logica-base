#hay que colocarle php -S localhost:8000 para que corra y luego en el navegador colocar http://localhost:8000/validaciones.php 
<?php

/**
 * Validar un formato estricto de correo electrónico.
 */
function validar_correo(string $email): bool {
    $correo_patron = "/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/";
    return (bool) preg_match($correo_patron, trim($email));
}

/**
 * Validar un formato de número telefónico (Operadoras venezolanas).
 */
function validar_telefono(string $telefono): bool {
    $telefono_patron = "/^(\+58|0)(412|414|424|416|426)\d{7}$/";
    $modificador_telefono = preg_replace("/[^\d+]/", "", trim($telefono));
    return (bool) preg_match($telefono_patron, $modificador_telefono);
}

/**
 * Validar formato de Cédula de Identidad.
 */
function validar_Cedula(string $cedula): bool {
    $cedula_patron = "/^[VEJ]?-?[0-9]{6,8}$|^[0-9]{6,8}$/";
    return (bool) preg_match($cedula_patron, trim($cedula));
}

/**
 * Función para DETECTAR un posible ataque XSS usando expresiones regulares.
 * Busca etiquetas HTML o atributos comunes de inyección.
 */
function detectar_XSS(string $entrada): bool {
    $patron_xss = "/<[^>]*>|javascript:|onerror=|onload=/i";
    return (bool) preg_match($patron_xss, $entrada);
}

/**
 * Aplicar sanitización básica para prevenir que el ataque rompa la interfaz.
 */
function sanitizacion_XSS(string $entrada): string {
    return htmlspecialchars(trim($entrada), ENT_QUOTES, 'UTF-8');
}


$email = $telefono = $cedula = "";
$errores = [];
$ataques_detectados = [];
$exito = false;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // 1. Recibimos los datos puros ingresados por el usuario
    $email_raw = $_POST['email'] ?? '';
    $telefono_raw = $_POST['telefono'] ?? '';
    $cedula_raw = $_POST['cedula'] ?? '';

    // 2. Filtro de Seguridad: Detectamos si hay intentos de ataque XSS
    if (detectar_XSS($email_raw)) $ataques_detectados[] = "Correo Electrónico";
    if (detectar_XSS($telefono_raw)) $ataques_detectados[] = "Teléfono";
    if (detectar_XSS($cedula_raw)) $ataques_detectados[] = "Cédula de Identidad";

    // 3. Sanitizamos los datos. Esto neutraliza las etiquetas HTML (<script>) 
    // convirtiéndolas en texto inofensivo para que no rompan el formulario.
    $email = sanitizacion_XSS($email_raw);
    $telefono = sanitizacion_XSS($telefono_raw);
    $cedula = sanitizacion_XSS($cedula_raw);

    // 4. Validaciones de Formato (expresiones regulares)
    if (empty($email)) {
        $errores['email'] = "El campo de correo no puede estar vacío.";
    } elseif (!validar_correo($email_raw)) {
        $errores['email'] = "El formato del correo ingresado no es válido.";
    }

    if (empty($telefono)) {
        $errores['telefono'] = "El campo de teléfono es obligatorio.";
    } elseif (!validar_telefono($telefono_raw)) {
        $errores['telefono'] = "El teléfono no coincide con un formato válido.";
    }

    if (empty($cedula)) {
        $errores['cedula'] = "Debe ingresar una cédula de identidad.";
    } elseif (!validar_Cedula($cedula_raw)) {
        $errores['cedula'] = "La estructura de la cédula es inválida.";
    }

    // 5. Verificamos si todo está correcto (sin errores de formato y sin ataques)
    if (empty($errores) && empty($ataques_detectados)) {
        $exito = true;
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reto 2: Filtros de Seguridad</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; padding: 20px; }
        .contenedor { max-width: 500px; margin: 0 auto; background: #fff; padding: 25px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .grupo-form { margin-bottom: 15px; }
[2/10/2026 10:46 p. m.] Luci-Brother: label { display: block; font-weight: bold; margin-bottom: 5px; color: #333; }
        input[type="text"] { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; }
        .error-msg { color: #d9534f; font-size: 0.85em; margin-top: 5px; display: block; font-weight: bold; }
        .input-error { border-color: #d9534f !important; background-color: #fdf0f0; }
        .btn { background: #0056b3; color: white; border: none; padding: 10px 20px; font-size: 1em; cursor: pointer; border-radius: 4px; width: 100%; font-weight: bold; }
        .btn:hover { background: #004494; }
        .alerta-exito { background: #dff0d8; color: #3c763d; padding: 15px; border-radius: 4px; margin-bottom: 20px; border: 1px solid #d6e9c6; }
        .alerta-peligro { background: #f2dede; color: #a94442; padding: 15px; border-radius: 4px; margin-bottom: 20px; border: 1px solid #ebccd1; }
    </style>
</head>
<body>

<div class="contenedor">
    <h2 style="text-align: center; margin-top: 0;">Filtros y Validación</h2>

    <!-- Bloque de alerta si se detecta un ataque XSS -->
    <?php if (!empty($ataques_detectados)): ?>
        <div class="alerta-peligro">
            <strong>¡Alerta de Seguridad (XSS)!</strong><br> 
            Se ha detectado un intento de inyección de código en los siguientes campos: 
            <ul>
                <?php foreach($ataques_detectados as $campo_atacado): ?>
                    <li><?= $campo_atacado ?></li>
                <?php endforeach; ?>
            </ul>
            Los datos maliciosos han sido neutralizados.
        </div>
    <?php endif; ?>

    <!-- Bloque de éxito -->
    <?php if ($exito): ?>
        <div class="alerta-exito">
            <strong>¡Validación Exitosa!</strong><br> 
            Todos los datos cumplen con los formatos estrictos y están libres de código malicioso.
        </div>
    <?php endif; ?>

    <form action="<?= htmlspecialchars($_SERVER["PHP_SELF"]) ?>" method="POST">
        
        <div class="grupo-form">
            <label for="email">Correo Electrónico:</label>
            <input type="text" id="email" name="email" value="<?= $email ?>" class="<?= isset($errores['email']) ? 'input-error' : '' ?>" placeholder="ejemplo@correo.com">
            <?php if (isset($errores['email'])): ?>
                <span class="error-msg"><?= $errores['email'] ?></span>
            <?php endif; ?>
        </div>

        <div class="grupo-form">
            <label for="telefono">Teléfono:</label>
            <input type="text" id="telefono" name="telefono" value="<?= $telefono ?>" class="<?= isset($errores['telefono']) ? 'input-error' : '' ?>" placeholder="0414-1234567">
            <?php if (isset($errores['telefono'])): ?>
                <span class="error-msg"><?= $errores['telefono'] ?></span>
            <?php endif; ?>
        </div>

        <div class="grupo-form">
            <label for="cedula">Cédula de Identidad:</label>
            <input type="text" id="cedula" name="cedula" value="<?= $cedula ?>" class="<?= isset($errores['cedula']) ? 'input-error' : '' ?>" placeholder="V-12345678">
            <?php if (isset($errores['cedula'])): ?>
                <span class="error-msg"><?= $errores['cedula'] ?></span>
            <?php endif; ?>
        </div>

        <button type="submit" class="btn">Procesar Datos</button>
    </form>
</div>

</body>
</html>
 hay que colocarle php -S localhost:8000 para que corra y luego en el navegador colocar http://localhost:8000/validaciones.php 