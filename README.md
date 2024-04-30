# PubSub-Bootcamp

---

## Requisitos previos a la clase

### Instalar Docker Desktop y Configurar una Cuenta en Docker Hub

*   Descarga e instala Docker Desktop desde el [sitio web oficial de Docker](https://docs.docker.com/engine/install/).

*   Una vez instalado, crea o inicia sesión en tu cuenta de Docker Hub.

*   Abre Docker Desktop e inicia sesión con tus credenciales de Docker Hub.

### Instala Redis

*   Ejecuta el siguiente comando en tu terminal para descargar la imagen Docker:
    ```
    docker pull redis:latest
    ```
    
### Prueba que todo este correcto

*   Ejecuta el siguiente comando en tu terminal para correr el contenedor
    ```	
    docker run --name testing-redis -p 6379:6379 -d redis
    ```

*   Ejecuta el siguiente comando en tu terminal para instalar redis
    ```	
    pip install redis
    ```

*   Ejecuta el siguiente script de python para validar que redis esta corriendo correctamente
    ```python
    from redis import StrictRedis
    def main():
        redis = StrictRedis(host="localhost", port="6379", db=0)
        redis.set("name", "Ulises")
        print(redis.get("name"))
        print(redis.exists("name"))
        print(redis.exists("age"))
    if __name__ == '__main__':
        main()
    ```

Si todo esta correcto, al ejecutarlo tu terminal deberia verse algo asi:
```
b'Ulises'
1
0
```

## Construir un API REST con Django REST Framework

Crea un ambiente virtual:
```
python3 -m venv env
```

Activa el ambiente virtual:
```
# Activación en Unix
source env/bin/activate

# Activación en Windows
env\Scripts\activate
```

Instala Django, DRF y PyJWT:
```
pip install channels
pip install channels-redis
pip install django
pip install djangorestframework
pip install redis
```

Crea un nuevo proyecto en Django:
```
django-admin startproject realtime_notifications
```

Crea una nueva aplicación en Django:
```
python manage.py startapp api
```

Agrega la aplicación de `rest_framework` y la que acabamos de crear en el archivo de `settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api'
]
```

Genera las migraciones y ejeculatas
```
python manage.py makemigrations
python manage.py migrate
```

Crea un super usuario
```
python manage.py createsuperuser
```

Corre la aplicación para corroborar que todo esta correcto
```
python manage.py runserver
```