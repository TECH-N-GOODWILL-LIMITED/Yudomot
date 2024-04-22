from flask import Flask, request, jsonify
import requests

# Create a Flask app instance
app = Flask(__name__)

#from maytapi to integrate with api
url = "https://api.maytapi.com/api/05236d2e-c3a9-4330-8b94-0f035a25b9c0/50857/sendMessage"
payload = "{\"to_number\": \"+23278090384\",\"type\": \"text\",\"message\": \"Happy Birthday Bredda\"}"
headers = {
    'x-maytapi-key': "b5983ccc-a610-46a4-8674-3a83c6bbd41b",
    'content-type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

#webhook callback implementation





# Define a route and a view function
#@app.route('/', methods=['GET'])
#def index():
 #   return "Welcome To Our Whatsapp Bot"

# Run the app
#if __name__ == '__main__':
 #   app.run(debug=True)
