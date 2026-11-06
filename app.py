from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/style.css")
def css():
    return send_from_directory(BASE_DIR, "style.css")

@app.route("/script.js")
def js():
    return send_from_directory(BASE_DIR, "script.js")


@app.route("/convert", methods=["POST"])
def convert():

    data = request.get_json()

    category = data.get("category")
    value = float(data.get("value"))
    from_unit = data.get("from_unit")
    to_unit = data.get("to_unit")

    units = {
        "Voltage": {
            "V": 1,
            "mV": 0.001,
            "kV": 1000
        },

        "Current": {
            "A": 1,
            "mA": 0.001,
            "uA": 0.000001
        },

        "Power": {
            "W": 1,
            "kW": 1000,
            "MW": 1000000
        },

        "Energy": {
            "J": 1,
            "kJ": 1000,
            "Wh": 3600,
            "kWh": 3600000
        }
    }

    try:
        factors = units[category]

        result = value * factors[from_unit] / factors[to_unit]

        return jsonify({
            "result": round(result, 8),
            "unit": to_unit
        })

    except (KeyError, TypeError, ValueError):
        return jsonify({
            "error": "Invalid conversion"
        }), 400


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
