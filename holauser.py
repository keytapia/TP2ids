from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/hola")
def hola():
    nombre = request.args.get("nombre")
    return f"Hola {nombre}"

if __name__ == "__main__":
    app.run(port=8080, debug=True)
