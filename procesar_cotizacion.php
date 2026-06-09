<?php
header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

// 🛑 CREDENCIALES DE BASE DE DATOS (Cuando suba a Hostinger, debe cambiar estas 3 líneas) 🛑
$host = 'localhost';
$usuario = 'root'; 
$password = ''; 
$base_datos = 'costalink_db';

$conexion = new mysqli($host, $usuario, $password, $base_datos);

if ($conexion->connect_error) {
    die(json_encode(["status" => "error", "message" => "Error de conexión a la base de datos"]));
}

$nombre = $_POST['nombre'] ?? '';
$email = $_POST['email'] ?? '';
$telefono = $_POST['telefono'] ?? '';
$tipo_persona = $_POST['tipo_persona'] ?? '';
$servicio_interes = $_POST['servicio_interes'] ?? '';
$tipo_vehiculo = $_POST['tipo_vehiculo'] ?? '';
$mensaje = $_POST['mensaje'] ?? '';

$stmt = $conexion->prepare("INSERT INTO cotizaciones (nombre, email, telefono, tipo_persona, servicio_interes, tipo_vehiculo, mensaje) VALUES (?, ?, ?, ?, ?, ?, ?)");
$stmt->bind_param("sssssss", $nombre, $email, $telefono, $tipo_persona, $servicio_interes, $tipo_vehiculo, $mensaje);

if ($stmt->execute()) {
    echo json_encode(["status" => "success"]);
} else {
    echo json_encode(["status" => "error"]);
}

$stmt->close();
$conexion->close();
?>