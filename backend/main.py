from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import mysql.connector
import shutil
import os
import uuid 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CARPETA_UPLOADS = "curriculum_archivos"
os.makedirs(CARPETA_UPLOADS, exist_ok=True) 

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="", 
        database="costalink_db"
    )

@app.post("/subir-postulacion/")
async def subir_postulacion(
    nombre: str = Form(...),
    email: str = Form(...),
    tipo_persona: str = Form("natural"), 
    documento: str = Form(""), 
    servicio_interes: str = Form(""),
    mensaje: str = Form(""),
    archivo_cv: UploadFile = File(...)
):
    try:
        extension = os.path.splitext(archivo_cv.filename)[1]
        nombre_unico_archivo = f"{uuid.uuid4()}{extension}"
        ruta_final_archivo = f"{CARPETA_UPLOADS}/{nombre_unico_archivo}"
        
        with open(ruta_final_archivo, "wb") as buffer:
            shutil.copyfileobj(archivo_cv.file, buffer)

        conexion = conectar_db()
        cursor = conexion.cursor()
        
        sql = """INSERT INTO postulaciones 
                 (nombre, email, tipo_persona, documento, servicio_interes, mensaje, archivo_cv_ruta) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        valores = (nombre, email, tipo_persona, documento, servicio_interes, mensaje, ruta_final_archivo)
        
        cursor.execute(sql, valores)
        conexion.commit() 
        
        cursor.close()
        conexion.close()
        
        return {"status": "exito", "mensaje": f"¡Excelente {nombre}! Información recibida correctamente."}
        
    except Exception as e:
        return {"status": "error", "mensaje": f"Error: {e}"}