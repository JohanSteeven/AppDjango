# Sistema de Gestión de Tareas Académicas

Bienvenido al **Sistema de Gestión de Tareas Académicas**, una aplicación web desarrollada con **Django** que permite a estudiantes gestionar sus entregas mediante un sistema CRUD (Crear, Leer, Actualizar, Eliminar).

## 🚀 Características

*   **Gestión de Tareas**: Crea, lista, edita y elimina tareas.
*   **Prioridades**: Clasifica tareas como Baja, Media o Alta.
*   **Estados**: Marca tareas como Completadas o Pendientes.
*   **Interfaz Gráfica**: Diseño limpio y responsivo utilizando **Bootstrap 5**.
*   **Validaciones**: Formularios robustos que aseguran la consistencia de los datos.

## 🛠️ Tecnologías Utilizadas

*   **Python**: Lenguaje de programación principal.
*   **Django**: Framework web de alto nivel.
*   **SQLite**: Base de datos por defecto (integrada en Django).
*   **Bootstrap 5**: Framework CSS para el diseño frontend.

## 📋 Requisitos Previos

*   Python 3.8 o superior instalado en tu sistema.
*   Pip (gestor de paquetes de Python).

## ⚙️ Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1.  **Clonar el repositorio** (o descargar el código fuente):
    ```bash
    git clone https://github.com/JohanSteeven/AppDjango
    cd AppDjango
    ```

2.  **Crear un entorno virtual (Opcional pero recomendado)**:
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install django
    ```

4.  **Aplicar migraciones**:
    Crea la base de datos SQLite y las tablas necesarias.
    ```bash
    python manage.py migrate
    ```

## ▶️ Ejecución

Para iniciar el servidor de desarrollo, ejecuta el siguiente comando en la terminal:

```bash
python manage.py runserver
```

Una vez iniciado, abre tu navegador web y visita:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📂 Estructura del Proyecto

*   `gestion_tareas/`: Configuración principal del proyecto Django.
*   `tareas/`: Aplicación que contiene la lógica (Modelos, Vistas, Forms).
*   `templates/`: Archivos HTML (Base, Lista, Detalle, Formulario).
*   `db.sqlite3`: Archivo de base de datos local.

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor crea un *fork* y envía un *pull request*.

---
Desarrollado con fines educativos para el aprendizaje de Django.
