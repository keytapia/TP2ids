from flask import Flask
app = Flask(__name__)
@app.route("/")

def index():
    return " patata "
if __name__  == '__main__':
    app.run(port=8080, debug=True)
