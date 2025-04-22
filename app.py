from flask import Flask, jsonify
import pandas as pd
import requests
from io import BytesIO

app = Flask(__name__)

EXCEL_URL = "https://drive.google.com/uc?export=download&id=1xuOA27tE4N1AkAMEqff54cd8moPfXCLh"

@app.route("/", methods=["GET"])
def home():
    return "Bienvenue sur l'API publique Cave Vivino 🥂", 200

@app.route("/api/cave", methods=["GET"])
def get_cave():
    try:
        response = requests.get(EXCEL_URL)
        if response.status_code != 200:
            return jsonify({"error": f"Fichier introuvable. Status {response.status_code}"}), 500

        df = pd.read_excel(BytesIO(response.content))
        return jsonify(df.to_dict(orient="records"))

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)