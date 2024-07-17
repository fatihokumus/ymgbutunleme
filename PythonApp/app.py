from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS'u tüm uygulama için etkinleştir


def predict_origin(first_name, last_name):
    # Türkçe karakterleri içeren isimler için kontrol
    turkish_chars = 'çğıöşüÇĞİÖŞÜ'
    if any(char in first_name for char in turkish_chars) or any(char in last_name for char in turkish_chars):
        return "Türkiye"
    
    # Basit kural tabanlı tahminler
    if first_name.lower().endswith('o') and last_name.lower().endswith('i'):
        return "İtalya"
    elif first_name.lower().endswith('a') and last_name.lower().endswith('a'):
        return "İspanya"
    elif first_name.lower().endswith('u') and last_name.lower().endswith('o'):
        return "Japonya"
    elif first_name.lower().endswith('e') and last_name.lower().endswith('r'):
        return "Almanya"
    elif first_name.lower().endswith('y') and last_name.lower().endswith('n'):
        return "USA"
    else:
        return "Üzgünüm Bulamadım"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    first_name = data['firstName']
    last_name = data['lastName']
    origin = predict_origin(first_name, last_name)
    return jsonify({'origin': origin})

if __name__ == '__main__':
    app.run(host='localhost', port=5000)