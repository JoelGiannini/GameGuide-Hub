# 🎮 GameGuide Hub

Plataforma web colaborativa desarrollada en **Django** diseñada para la gestión integral de catálogos de videojuegos, plataformas y guías de juego comunitarias. Este proyecto cumple con los requisitos del trabajo práctico final, estructurando la arquitectura de manera modular en múltiples aplicaciones reutilizables.

---

## 📹 Demostración en Video

A continuación se muestra la demostración de la aplicación en funcionamiento:

<video src="preview_app.mp4" controls width="100%" poster="">
  Tu navegador no soporta la reproducción de video. Podés ver el archivo <a href="preview_app.mp4">preview_app.mp4</a> directamente en el repositorio.
</video>

---

## 🏛️ Estructura del Proyecto y Requisitos Técnicos

El desarrollo se encuentra modularizado bajo buenas prácticas de arquitectura Django, dividiendo las responsabilidades lógicas en **4 aplicaciones customizadas**:

1. **`core`**: Gestiona las vistas generales del sitio, la página de inicio, las secciones estáticas y el enrutamiento base.
2. **`catalog`**: Administra el catálogo de plataformas de videojuegos (ej. SEGA, Nintendo, etc.) y los títulos disponibles.
3. **`guides`**: Contiene la lógica, modelos y vistas orientadas a la creación, lectura y administración de guías y tutoriales de juegos.
4. **`interaction`**: Administra la interacción de los usuarios dentro de la plataforma (comentarios, valoraciones o formularios de contacto).

---

## 🚀 Guía de Instalación y Ejecución Local

Para levantar y probar el proyecto en tu entorno local, seguí estos pasos desde la terminal:

### 1. Clonar el repositorio
```bash
git clone https://github.com/JoelGiannini/GameGuide-Hub.git
cd GameGuide-Hub
```

### 2. Crear y activar el entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate  # En Windows usar: venv\Scripts\activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar las migraciones de la Base de Datos
```bash
python manage.py migrate
```

### 5. Crear un Superusuario (para acceder al panel de administración)
```bash
python manage.py createsuperuser
```
*(Ingresá tu nombre de usuario, correo y contraseña cuando se te solicite).*

### 6. Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

Una vez iniciado el servidor, abrí tu navegador e ingresá a:
* **Sitio Web Principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Panel de Administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (accedé con las credenciales creadas en el paso 5 para cargar plataformas, juegos y guías de prueba).
