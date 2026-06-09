<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

// 🛑 CREDENCIALES DE BASE DE DATOS 🛑
$host = 'localhost';
$usuario = 'root'; 
$password = ''; 
$base_datos = 'costalink_db';

$conexion = new mysqli($host, $usuario, $password, $base_datos);

$nombre = $_POST['nombre'] ?? '';
$email = $_POST['email'] ?? '';
$telefono = $_POST['telefono'] ?? '';
$cedula = $_POST['cedula'] ?? '';
$cargo = $_POST['cargo'] ?? '';
$licencia = $_POST['licencia'] ?? '';
$perfil = $_POST['perfil'] ?? '';

// Crear la carpeta para los PDFs si no existe
$directorio_subida = 'hojas_de_vida/';
if (!file_exists($directorio_subida)) {
    mkdir($directorio_subida, 0777, true);
}

$ruta_archivo = '';

// Guardar el PDF con la cédula en el nombre para que no se pierda
if (isset($_FILES['hoja_vida']) && $_FILES['hoja_vida']['error'] === UPLOAD_ERR_OK) {
    $nombre_limpio = str_replace(' ', '_', basename($_FILES['hoja_vida']['name']));
    $nombre_final = $cedula . '_' . time() . '_' . $nombre_limpio; 
    $ruta_archivo = $directorio_subida . $nombre_final;
    
    move_uploaded_file($_FILES['hoja_vida']['tmp_name'], $ruta_archivo);
}

$stmt = $conexion->prepare("INSERT INTO postulaciones (nombre, email, telefono, cedula, cargo, licencia, perfil, ruta_archivo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)");
$stmt->bind_param("ssssssss", $nombre, $email, $telefono, $cedula, $cargo, $licencia, $perfil, $ruta_archivo);

if ($stmt->execute()) {
    echo json_encode(["status" => "success"]);
} else {
    echo json_encode(["status" => "error"]);
}

$stmt->close();
$conexion->close();
?>