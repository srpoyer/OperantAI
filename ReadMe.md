# Twilio API Listener

## Overview
This is a Flask-based REST API that listens for incoming POST requests on port `8001`. It processes incoming data and sends it as an SMS message using Twilio. Any data received in the POST request is formatted into a message body and forwarded to Twilio.

## Features
- Accepts any form-encoded POST data from clients.
- Sends received data as an SMS message via Twilio.
- Configurable via environment variables.

## Requirements
- Python 3.9+
- Twilio account with API credentials
- Flask and Requests libraries

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/twilio-api-listener.git
   cd twilio-api-listener
   ```

2. Set up a virtual environment (optional but recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
Set the following environment variables:

```sh
export TWILIO_URL="https://api.twilio.com/2010-04-01/Accounts/YOUR_ACCOUNT_SID/Messages.json"
export TWILIO_ACCOUNT_SID="your_account_sid"
export TWILIO_AUTH_TOKEN="your_auth_token"
export MESSAGE_TO="recipient_phone_number"
export MESSAGE_FROM="your_twilio_phone_number"
```

## Running the Application
Start the Flask server:
```sh
python twilio_listener.py
```

## Testing the API
Send a POST request with sample data:
```sh
curl -X POST http://127.0.0.1:8001/message -d "phone_number=18005551212"
```

Expected response:
```json
{
  "status": 201,
  "response": "Message sent successfully"
}
```
Alternatively, you can import and use the included Insomnia Request Collection

## Running with Docker
1. Set up your variables in the your.env file and then rename to ".env"

2. Build the Docker image:
   ```sh
   docker build -t twilio-listener .
   ```
3. Run the container:
   ```sh
   docker run -p 8001:8001 --env-file .env twilio-listener
   ```

## License
MIT License

