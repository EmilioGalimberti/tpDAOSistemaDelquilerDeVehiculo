# /run.py
from sistema import app

if __name__ == '__main__':
    # debug=True activa el modo de depuración.
    # El servidor se reiniciará automáticamente con cada cambio
    # y mostrará errores detallados en el navegador.
    app.run(debug=True)