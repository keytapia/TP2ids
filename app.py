from flask import request
app = Flask(__name__)
@app.route("/hola")
def hola():
    nombre = request.args.get("nombre")
    return f"Hola {nombre}"
