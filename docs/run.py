#para arrancar el servidor y visualizar en postman o navegador
from TP2ids.docs.app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    