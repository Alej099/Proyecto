# Proyecto
Proyecto “Desarrollo de un Motor de Recomendaciones de Libros Basado en Redes Neuronales”

estructura en django 
instalacion Django 
visual terminal 
verificar instalacion de python comando:   python --version
verificar instalacion postgres 
instalar Django: pip install django psycopg2
ir a pgadmin crear una base de datos vacia llamada Libreria_bd
crear usuario postgres asignar todos los permisos y colocarle contraseña 1234
en los archivos de la (libreria mirar estructura) ir a settings.py 
cambiar usuario por su usuario 
migracion de basa de datos django a postgres: python manage.py makemigrations lib_general
python manage.py migrate
python manage.py runserver



libreria/                  # Proyecto principal
├── libreria/              # Configuración del proyecto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Aquí se registra 'lib_general'
│   ├── urls.py            # Aquí se incluyen las rutas de lib_general
│   └── wsgi.py
├── manage.py

# App única que maneja todo: usuarios, libros, calificaciones, interacciones
├── lib_general/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py           # Formularios de registro, login, etc.
│   ├── migrations/
│   ├── models.py          # Aquí van todas las clases: Usuario, Libro, Interacción,recomendacion, neurona y busqueda ppl
│   ├── tests.py
│   ├── urls.py            # Enrutamiento para todas las vistas
│   ├── views.py           # Vistas para todo: login, registro, libros, calificaciones, etc.
│   └── templates/
│       └── lib_general/
│           ├── index 
│           ├── login.html
│           ├── registro.html
│           ├── calificar.html
│           └── interaccion.html
    └── static/
│       └── imgenes/
        └── css/
        └── js/  escrip

