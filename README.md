# 🎮 GameGuide Hub

Plataforma web colaborativa desarrollada en **Django** diseñada para la gestión integral de catálogos de videojuegos, plataformas y guías de juego comunitarias.

---

## 📹 Demostración en Video

Podés ver la demostración en video de la aplicación en funcionamiento directamente desde el repositorio:

👉 **[Descargar demostración de la app funcionando en video (preview_app.mp4)](./preview_app.mp4)**

---

## 🏛️ Estructura del Proyecto y Requisitos Técnicos

El proyecto cumple ampliamente con el requisito de contar con **al menos 8 aplicaciones**, integrando las **6 aplicaciones nativas de Django** junto a **4 aplicaciones customizadas**:

### Aplicaciones Customizadas:
1. **`core`**: Vistas generales del sitio, landing page, páginas estáticas y enrutamiento principal.
2. **`catalog`**: Gestión del catálogo de plataformas de videojuegos y títulos disponibles.
3. **`guides`**: Lógica, modelos y vistas para la administración y lectura de guías de juego.
4. **`interaction`**: Formularios de contacto, valoraciones y gestión de interacciones con el usuario.

### Aplicaciones Nativas de Django (Incluidas):
5. `django.contrib.admin`
6. `django.contrib.auth`
7. `django.contrib.contenttypes`
8. `django.contrib.sessions`
9. `django.contrib.messages`
10. `django.contrib.staticfiles`

---

## 🚀 Guía de Instalación y Ejecución Local

Para levantar y probar el proyecto en tu entorno local:

### 1. Clonar el repositorio
```bash
git clone https://github.com/JoelGiannini/GameGuide-Hub.git
cd GameGuide-Hub
```

### 2. Crear y activar el entorno virtual
```bash
python3 -m venv venv
<<<<<<< HEAD
source venv/bin/activate  # En Windows: venv\Scripts\activate
=======
source venv/bin/activate 
>>>>>>> c23d2b1bcf7102acb11570a8f7abb1d7282ffe17
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones
```bash
python manage.py migrate
```

### 5. Crear Superusuario (opcional si se usa la DB provista)
```bash
python manage.py createsuperuser
```

### 6. Iniciar el Servidor
```bash
python manage.py runserver
```

Rutas locales para pruebas:
* **Sitio Principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Panel de Administración:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
