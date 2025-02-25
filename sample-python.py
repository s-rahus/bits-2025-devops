from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, BITS Pilani"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        'name': 'Flask',
        'type': 'Web Framework',
        'language': 'Python'
    }
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    new_data = request.json
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(debug=True)
