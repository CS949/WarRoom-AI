from flask import Flask
from flask_cors import CORS

from routes.analyze import analyze_bp
from routes.history import history_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    analyze_bp
)

app.register_blueprint(
    history_bp
)

@app.route("/")
def home():

    return {

        "message":
        "WarRoom AI Backend Running"

    }

if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )