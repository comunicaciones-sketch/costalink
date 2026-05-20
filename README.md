# 🚐 Costa Link S.A.S. - Performance Mobility Web Platform

Plataforma web corporativa y sistema de recepción de solicitudes para **Transportes Costa Link S.A.S.**, empresa especializada en transporte público terrestre especial de pasajeros y de carga a nivel nacional.

## ✨ Características Principales

* **Diseño Ultra Premium (UI/UX):** Interfaz moderna con diseño limpio, menús estilo "Dynamic Island" (flotantes), Hero encapsulado con video de fondo y paleta de colores corporativa.
* **Interactividad 3D y Animaciones:** Tarjetas de servicios interactivas con inclinación física 3D (`Vanilla-Tilt.js`) y elementos que aparecen suavemente al hacer scroll (`AOS.js`).
* **Gestor de Solicitudes y Empleo:** Formulario de contacto conectado a backend para procesar cotizaciones de servicios y recepción de Hojas de Vida (archivos PDF/DOCX).
* **Almacenamiento Local:** Guardado seguro de documentos adjuntos con identificadores únicos (UUID) para evitar sobrescritura de archivos.

## 🛠️ Tecnologías y Stack

**Frontend:**
* HTML5 & CSS3 (Flexbox/Grid, Glassmorphism)
* Vanilla JavaScript
* [AOS (Animate On Scroll)](https://michalsnik.github.io/aos/)
* [Vanilla-Tilt.js](https://micku7zu.github.io/vanilla-tilt.js/)
* FontAwesome (Iconografía)

**Backend & Base de Datos:**
* Python 3
* [FastAPI](https://fastapi.tiangolo.com/) (Framework web de alto rendimiento)
* Uvicorn (Servidor ASGI)
* MySQL (Vía XAMPP para desarrollo local)
* `mysql-connector-python` & `python-multipart`

## 📁 Estructura del Proyecto

```text
proyecto_costalink/
├── backend/
│   ├── main.py                  # API y lógica de servidor en FastAPI
│   └── curriculum_archivos/     # Directorio autogenerado para guardar PDFs
├── frontend/
│   ├── index.html               # Landing page principal
│   ├── servicio-*.html          # Vistas detalladas de los 6 servicios
│   ├── style.css                # Estilos globales y responsive design
│   └── img/                     # Assets (Logo, imágenes, video de fondo)
├── .gitignore                   # Exclusiones para el control de versiones
└── README.md                    # Documentación del proyecto
