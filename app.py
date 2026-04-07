from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return 'Prueba Hola Mundo'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
