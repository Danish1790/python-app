from flask import Flask, jsonify

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "<h1>Welcome to My Flask App!</h1>"

# Simple API route
@app.route('/api/hello', methods=['GET'])
def api_hello():
    return jsonify(message="Hello from Flask API!")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
