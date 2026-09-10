# SpyInstaComments

Aplicación Django heredada para organizar y analizar comentarios de Instagram.

## Estado de esta rama

La rama `feat/local-safe-modernization` está preparada para ejecutar el proyecto localmente sin Docker en macOS Catalina/Python 3.10.

También se eliminó la validación que consultaba el endpoint antiguo de Instagram `?__a=1`, porque ya no es una API pública fiable y actualmente puede devolver errores 401 o bloqueos temporales.

## Alcance

Usar únicamente comentarios públicamente visibles, datos propios, exportaciones propias o integraciones para las que tengas autorización. Esta rama no intenta acceder a perfiles privados, mensajes directos, contraseñas, cookies ni sesiones de terceros.

## Instalación local en macOS

```bash
cd /Volumes/Armazenamento/developer
git clone https://github.com/sebastisnzoth/SpyInstaComments.git
cd SpyInstaComments
git checkout feat/local-safe-modernization

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

## Base de datos

El repositorio incluye una base SQLite heredada. Para una instalación limpia es preferible crear una base nueva localmente:

```bash
mv db.sqlite3 db.sqlite3.legacy 2>/dev/null || true
python3 manage.py migrate
python3 manage.py createsuperuser
```

## Ejecutar

```bash
python3 manage.py runserver 127.0.0.1:8000
```

Abrí en el navegador:

```text
http://127.0.0.1:8000
```

## Dependencias

- Django 3.2.25
- requests 2.x

Se fijó Django 3.2.x para mantener compatibilidad con el código original, generado alrededor de Django 3.1, y con Python 3.10.

## Próximo paso recomendado

Reemplazar la lógica antigua de scraping de Instagram por una fuente autorizada o por importación local de CSV/JSON con comentarios exportados. De esa forma la interfaz de monitoreo puede seguir utilizándose sin depender de endpoints privados o inestables de Instagram.
