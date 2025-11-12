# /sistema/controllers/alquiler_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from sistema import db
from sistema.models.vehiculo import Vehiculo
from sistema.models.cliente import Cliente
from sistema.models.empleado import Empleado
from sistema.models.alquiler import Alquiler
from sistema.models.modelo import Modelo  # Importamos para la consulta
from sistema.models.marca import Marca  # Importamos para la consulta

# Creamos el Blueprint para la transacción de alquiler
alquiler_bp = Blueprint('alquiler', __name__)


@alquiler_bp.route('/')
def listar_alquileres():
    """
    Ruta para mostrar la lista de todos los alquileres.
    """
    try:
        # 1. Obtenemos todos los alquileres.
        #    Usamos 'joinedload' para traer los datos relacionados
        #    (cliente, vehiculo, modelo, marca) en una sola consulta.
        alquileres = Alquiler.query.options(
            db.joinedload(Alquiler.cliente),
            db.joinedload(Alquiler.vehiculo).joinedload(Vehiculo.modelo).joinedload(Modelo.marca)
        ).order_by(Alquiler.fecha_inicio.desc()).all()

        # 2. Renderizamos la plantilla (que crearemos en el sig. paso)
        return render_template('alquiler/listado.html', alquileres=alquileres)

    except Exception as e:
        flash(f'Error al cargar la lista de alquileres: {e}', 'danger')
        return redirect(url_for('main.index'))

@alquiler_bp.route('/nuevo', methods=['GET', 'POST'])
def registrar_alquiler():
    """
    Ruta para la transacción principal: registrar un nuevo alquiler.
    Maneja tanto la visualización del formulario (GET)
    como el procesamiento de los datos (POST).
    """

    # --- Lógica para el method POST (Cuando se envía el formulario) ---
    if request.method == 'POST':
        # 1. Obtener datos del formulario
        id_vehiculo = request.form.get('id_vehiculo')
        id_cliente = request.form.get('id_cliente')
        # (Simulamos que el empleado 1 es el que hace la operación) TODO Esto podemos hacer una sesion
        id_empleado = 1

        # 2. Buscar los objetos en la BD
        vehiculo = Vehiculo.query.get(id_vehiculo)
        cliente = Cliente.query.get(id_cliente)
        empleado = Empleado.query.get(id_empleado)

        if not vehiculo or not cliente or not empleado:
            flash('Error: Vehículo, Cliente o Empleado no encontrado.', 'danger')
            return redirect(url_for('alquiler.registrar_alquiler'))

        # --- 3. ¡ PROBAMOS EL PATRÓN STATE! ---
        try:
            # 3a. Intentamos la acción.
            # El objeto Vehiculo (y su estado) decidirá si esto es válido.
            vehiculo.alquilar()

            # 3b. Si tuvo éxito (no hubo excepción), creamos la transacción
            nuevo_alquiler = Alquiler(
                id_cliente=id_cliente,
                id_empleado=id_empleado,
                id_vehiculo=id_vehiculo
                # El estado 'Activo' y la fecha_inicio son por default
            )

            db.session.add(nuevo_alquiler)

            # db.session.commit() guardará AMBAS cosas:
            # 1. El nuevo estado del Vehiculo (ej. 'Alquilado')
            # 2. El nuevo registro de Alquiler
            db.session.commit()

            flash('¡Alquiler registrado exitosamente!', 'success')
            # Redirigimos a la lista de vehículos para ver el cambio de estado
            return redirect(url_for('vehiculos.listar_vehiculos'))

        except Exception as e:
            # 3c. Si el estado (ej. 'Alquilado') lanzó un error:
            db.session.rollback()  # Revertimos cualquier cambio
            flash(f'Error al alquilar: {e}', 'danger')
            # Volvemos a mostrar el formulario con el error
            return redirect(url_for('alquiler.registrar_alquiler'))

    # --- Lógica para el metodo GET (Mostrar el formulario) ---
    try:
        # Pasamos solo los vehículos DISPONIBLES al formulario
        vehiculos_disponibles = Vehiculo.query.filter_by(estado='Disponible').all()
        clientes = Cliente.query.all()

        return render_template('alquiler/nuevo.html',
                               vehiculos=vehiculos_disponibles,
                               clientes=clientes)
    except Exception as e:
        flash(f'Error al cargar el formulario: {e}', 'danger')
        return redirect(url_for('main.index'))

# (Aquí también iría la ruta para 'Registrar Devolución',
#  que llamaría a vehiculo.devolver() y finalizaría el alquiler)