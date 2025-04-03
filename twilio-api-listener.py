from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

TWILIO_URL = os.getenv("TWILIO_URL")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
MESSAGE_TO = os.getenv("MESSAGE_TO")
MESSAGE_FROM = os.getenv("MESSAGE_FROM")

def send_sms(message_body):
    payload = {
        "To": MESSAGE_TO,
        "From": MESSAGE_FROM,
        "Body": message_body
    }
    response = requests.post(TWILIO_URL, data=payload, auth=(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN))
    return response.status_code, response.text

@app.route("/message", methods=["POST"])
def handle_message():
    data = request.form.to_dict()
    message_body = "\n".join([f"{key}: {value}" for key, value in data.items()])
    
    if data:
        status_code, response_text = send_sms(message_body)
        return jsonify({"status": status_code, "response": response_text})
    
    return jsonify({"status": "no data received"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
