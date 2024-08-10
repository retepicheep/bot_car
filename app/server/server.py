from flask import Flask, jsonify
from flask_cors import CORS
# from sensors import ultrasonic
import os
app = Flask(__name__)
CORS(app)

@app.route("/api/home", methods=["GET"])
def return_home():
    return jsonify({
        "message": "Getting range to target..."
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)