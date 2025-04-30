from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'hrithik.krishna@kommunicate.io'
app.config['MAIL_PASSWORD'] = 'kqqd rwhu kxsw ujlg'
app.config['MAIL_DEFAULT_SENDER'] = 'hrithik.krishna@kommunicate.io'

mail = Mail(app)

@app.route('/', methods=['GET'])
def home():
    return [{"message": "Webhook Receiver Running"}]

@app.route('/webhook', methods=['POST'])
def webhook():
    # This function will be triggered by incoming webhook requests

    # Extract the data sent to the webhook
    data = request.json
    print("Received data:", data)

    # Check if the word "Hospital" is in the message
    if 'Hospital' in data.get('message', ''):
        # Send an email
        send_email(data)

    return jsonify([{"message": "Webhook triggered"}])

def send_email(data):
    # Create a message for the email
    subject = 'Hospital Alert'
    group_id = data.get('groupId', 'N/A')
    message_text = data.get('message', '')
    body = f"Webhook received with the message: {message_text}\nGroup ID: {group_id}"
    recipients = ['hrithikkrishna56@gmail.com']  # Replace with the actual recipient email address

    # Send the email
    msg = Message(subject=subject, body=body, recipients=recipients)
    mail.send(msg)

if __name__ == '__main__':
    app.run(port=5001, debug=True)
