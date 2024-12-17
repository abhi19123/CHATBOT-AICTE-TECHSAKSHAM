from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response
import traceback

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        text = request.get_json().get("message")
        if not text:
            return jsonify({"error": "No message provided"}), 400

        response = get_response(text)
        message = {"answer": response}
        return jsonify(message)
    except Exception as e:
        print("Error:", str(e))
        print(traceback.format_exc())
        return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    try:
        print("Starting the chatbot server...")
        app.run(debug=True, host='0.0.0.0', port=5000)
    except Exception as e:
        print("Error starting server:", str(e))
        print(traceback.format_exc())