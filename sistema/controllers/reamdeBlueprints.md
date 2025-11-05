
## 🏛️ Blueprints: Modularización de Controladores

Una de las decisiones de arquitectura clave en este proyecto es el uso de **Blueprints** de Flask. Esta sección explica por qué los usamos y el problema que resuelven.

En términos técnicos, un **Blueprint** es un objeto que permite registrar un subconjunto de rutas y operaciones. No es una aplicación en sí misma, sino un **"paquete de rutas"** que define cómo manejar un grupo de URLs.

### El Problema (Sin Blueprints): El Controlador Monolítico

Si no usáramos Blueprints, todas las rutas del proyecto tendrían que definirse en el mismo lugar donde creamos la `app` (en `sistema/__init__.py`, dentro de la función `create_app`).

El código se vería así:

```python
# /sistema/__init__.py (EJEMPLO DE LO QUE EVITAMOS)

def create_app():
    app = Flask(__name__)
    # ...

    @app.route('/')
    def index():
        # ...
        
    @app.route('/marcas/')
    def listar_marcas():
        # Lógica para listar marcas
        
    @app.route('/marcas/nuevo')
    def crear_marca():
        # Lógica para crear una marca
    
    @app.route('/vehiculos/')
    def listar_vehiculos():
        # Lógica para listar vehículos
    
    @app.route('/vehiculos/nuevo')
    def crear_vehiculo():
        # Lógica para crear un vehículo
    
    # ... (Imagina 50 rutas más aquí) ...
    
    return app
````

Esto se conoce como un **"controlador monolítico"** y tiene graves desventajas:

  * **Mantenimiento Imposible:** El archivo `__init__.py` se vuelve gigantesco e ilegible.
  * **Alto Acoplamiento:** La lógica de `marcas` está completamente mezclada con la de `vehiculos`, `clientes`, etc.
  * **Falta de Separación de Conceptos (SoC):** Viola los principios básicos de un buen diseño.

-----

### La Solución (Con Blueprints): Controladores Modulares

Un Blueprint actúa como un **controlador** en un patrón MVC, permitiéndonos encapsular toda la lógica de una sección de la aplicación en su propio archivo.

Nuestra arquitectura funciona en dos pasos:

#### 1\. Definición (El Controlador)

En `sistema/controllers/marca_controller.py`, creamos una instancia de `Blueprint` y le "enseñamos" las rutas que le pertenecen *solo a él*.

```python
# /sistema/controllers/marca_controller.py

# 'marca_bp' es un objeto que colecciona rutas
marca_bp = Blueprint('marcas', __name__)

# Esta ruta pertenece solo a 'marca_bp'
@marca_bp.route('/')
def listar_marcas():
    # Lógica para listar marcas
    
@marca_bp.route('/nuevo')
def crear_marca():
    # Lógica para crear una marca
```

En este punto, la aplicación principal (`app`) no tiene idea de que estas rutas existen. `marca_bp` es solo un objeto desconectado.

#### 2\. Registro (La Fábrica)

En `sistema/__init__.py`, dentro de la "fábrica" (`create_app`), importamos y "registramos" el blueprint en la aplicación principal.

```python
# /sistema/__init__.py

def create_app():
    app = Flask(__name__)
    # ... (configuración de db)

    # Importamos el blueprint
    from .controllers.marca_controller import marca_bp
    
    # ¡LA MAGIA!
    # Registramos el blueprint en la app
    app.register_blueprint(marca_bp, url_prefix='/marcas')

    return app
```

### El Beneficio Clave: `url_prefix`

La magia ocurre con `url_prefix='/marcas'`. Este comando le dice a Flask:
"Toma todas las rutas definidas en `marca_bp` y **antepónles el string `/marcas`** antes de registrarlas".

**Resultado:**

  * En el controlador: `@marca_bp.route('/')` → Se registra en la app como: `/marcas/`
  * En el controlador: `@marca_bp.route('/nuevo')` → Se registra en la app como: `/marcas/nuevo`

En resumen, un Blueprint actúa como un **espacio de nombres (namespace)** para un grupo de rutas, permitiéndonos tener nuestro código de controladores (`/controllers/`) perfectamente ordenado, desacoplado y escalable.

```
```