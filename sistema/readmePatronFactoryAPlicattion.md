# ¿Qué es el Patrón "Application Factory"? (LO APLICAMOS AL CREAR LA APLICACION)
Sí, es un patrón de diseño de software. Es una implementación específica del Patrón Factory (Fábrica), que es uno de los patrones "clásicos" (de la Gang of Four).

## ¿Qué hace? 
En lugar de crear un objeto (nuestra app de Flask) en el momento en que se carga el archivo (lo que se llama "ámbito global"), creamos una función que fabrica y devuelve ese objeto (def create_app()).


## ¿Por qué lo usamos? 
(¡Esto es lo importante!) Resuelve un problema muy común en Flask llamado "importaciones circulares".

## El Problema:

Nuestro archivo __init__.py crea la app y también el objeto db (de SQLAlchemy).

Nuestros archivos de Modelos (como vehiculo.py) necesitan importar db desde __init__.py para definir las clases.

Nuestros archivos de Controladores (como vehiculo_controller.py) necesitan importar la app (para las rutas) y también los Modelos (para usarlos).

Si __init__.py intenta importar los Modelos (para registrarlos) y los Modelos importan db de __init__.py... ¡tenemos un círculo! Python no sabe qué archivo cargar primero.

## La Solución (La Fábrica):

En __init__.py, creamos db, pero no lo conectamos a ninguna app.

Los Modelos importan este db "vacío" sin problemas.

La función create_app():

Crea la app.

Conecta db a esa app (db.init_app(app)).

Importa y registra los Controladores (Blueprints).

Devuelve la app ya lista y ensamblada.

run.py simplemente llama a esa función para obtener la app.

Es como tener una línea de ensamblaje (create_app) en lugar de intentar construir un auto en medio del garaje (__init__.py global) donde todas las piezas intentan conectarse entre sí al mismo tiempo.