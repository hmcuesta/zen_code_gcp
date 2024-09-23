from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    required_fields = ['project', 'endpoint_id', 'location', 'instances']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    project = data['project']
    endpoint_id = data['endpoint_id']
    location = data['location']
    instances = data['instances']

    prediction = {
        "predicted_value": sum(instances.values())  # Example prediction logic
    }

    # Return the prediction as a JSON response
    return jsonify({
        "project": project,
        "endpoint_id": endpoint_id,
        "location": location,
        "prediction": prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
