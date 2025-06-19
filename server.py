from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate_area', methods=['POST'])
def calculate_area():
    data = request.get_json()
    
    if not data or 'radius' not in data:
        return jsonify({
            "status": "error",
            "message": "Radius is required"
        }), 400

    try:
        radius = float(data['radius'])
    except ValueError:
        return jsonify({
            "status": "error",
            "message": "Invalid radius"
        }), 400

    if radius < 0:
        return jsonify({
            "status": "error",
            "message": "Radius cannot be negative"
        }), 400

    area = 3.14159 * radius * radius

    return jsonify({
        "status": "success",
        "result": round(area, 2),
        "function": "calculate_circle_area"
    })

if __name__ == '__main__':
    app.run(debug=True)
