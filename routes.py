from flask import request, jsonify
from app import app
from app.marco import speak, takeCommand, wishMe

@app.route('/')
def home():
    return "Marco Assistant API is running!"

@app.route('/wish', methods=['GET'])
def api_wish():
    wishMe()
    return jsonify({"message": "Wished successfully!"})

@app.route('/command', methods=['POST'])
def api_command():
    data = request.get_json()
    command = data.get('command', '').lower()
    if not command:
        return jsonify({"error": "No command provided"}), 400

    if "stop" in command:
        speak("Shutting down, have a nice day!")
        return jsonify({"message": "Assistant stopped."})

    # Add more command processing here
    speak(f"Processing command: {command}")
    return jsonify({"message": f"Command '{command}' processed."})
