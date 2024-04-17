from flask import Flask, request, jsonify

# Create a Flask app instance
app = Flask(__name__)


# Define a route and a view function
@app.route('/', methods=['GET'])
def index():
    return "Welcome To Our Whatsapp Bot"


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
