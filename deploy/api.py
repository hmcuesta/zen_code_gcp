from flask import Flask, request, jsonify
from google.cloud import aiplatform


app = Flask(__name__)

# Configuración de Vertex AI Endpoint
project_id = 'xxxx'
model_endpoint_id = 'xxx'
location = 'us-central1'

@app.route('/predict-fraud', methods=['POST'])
def predict_fraud():
    try:
        data = request.get_json()
        print(data)
        instances = [data['instances']]
        
        client = aiplatform.gapic.PredictionServiceClient()
        endpoint = client.endpoint_path(project=project_id, location=location, endpoint=model_endpoint_id)
        
        prediction = client.predict(endpoint=endpoint, instances=instances)
        
        return jsonify({'fraud_probability': prediction.predictions[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    