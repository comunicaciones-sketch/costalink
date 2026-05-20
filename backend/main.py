from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import mysql.connector
import os
import uuid

app = FastAPI()

# Configuración CORS para que el frontend se pueda comunicar con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear la carpeta de archivos si no existe
CARPETA_ARCHIVOS = "curriculum_archivos"
os.makedirs(CARPETA_ARCHIVOS, exist_ok=True)

# Conexión a la base de datos MySQL (XAMPP)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # Por defecto XAMPP no tiene clave
        database="costalink_db"
    )

@app.post("/subir-postulacion/")
async def subir_postulacion(
    nombre: str = Form(...),
    email: str = Form(...),
    tipo_persona: str = Form(...),
    documento: Optional[str] = Form(None),
    servicio_interes: str = Form(...),
    tipo_vehiculo: str = Form(...), # 🛑 NUEVO CAMPO AGREGADO 🛑
    mensaje: Optional[str] = Form(None),
    archivo_cv: Optional[UploadFile] = File(None) # 🛑 AHORA ES OPCIONAL 🛑
):
    ruta_archivo = None

    # Si la persona subió un archivo, lo guardamos
    if archivo_cv and archivo_cv.filename:
        extension = os.path.splitext(archivo_cv.filename)[1]
        nombre_unico = f"{uuid.uuid4()}{extension}"
        ruta_archivo = os.path.join(CARPETA_ARCHIVOS, nombre_unico)
        
        with open(ruta_archivo, "wb") as buffer:
            buffer.write(await archivo_cv.read())

    # Guardar todo en la Base de Datos
    conexion = get_db_connection()
    cursor = conexion.cursor()

    sql = """
    INSERT INTO postulaciones 
    (nombre, email, tipo_persona, documento, servicio_interes, tipo_vehiculo, mensaje, archivo_cv_ruta) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = (nombre, email, tipo_persona, documento, servicio_interes, tipo_vehiculo, mensaje, ruta_archivo)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()

    return {"mensaje": "¡Excelente! Hemos recibido tu información exitosamente."}