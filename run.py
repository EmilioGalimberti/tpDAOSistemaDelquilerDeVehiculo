# /run.py
from sistema import create_app

# Llama a la factory para crear la aplicación
app = create_app()

if __name__ == '__main__':
    # debug=True es genial para desarrollo
    app.run(debug=True)