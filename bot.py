from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Get weather information from an external API
def get_weather():
    try:
        response = requests.get("https://api.weather.com/...")
        # Process the API response and extract relevant weather information
        weather_info = process_response(response)
        return weather_info
    except requests.RequestException:
        return "Sorry, unable to fetch weather information."

# Placeholder function to process API response
def process_response(response):
    # Implement your logic here to extract weather information from the response
    # Return the extracted information as a string
    return "Today's weather is sunny and warm."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get('user_input')
    response = ""

    if user_input:
        if "name" in user_input.lower():
            response = "You can call me ChatBot. How can I assist you?"
        elif "joke" in user_input.lower():
            response = "Sure! Why don't scientists trust atoms? Because they make up everything!"
        elif "weather" in user_input.lower():
            response = get_weather()
        elif "bye" in user_input.lower():
            response = "Goodbye! Have a great day!"
        else:
            response = "I'm sorry, I didn't understand. Can you please rephrase your query?"
    else:
        response = "Please provide some input."

    return jsonify({'bot_response': response}), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(port=5000)
