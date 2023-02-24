from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_webhook():
    if request.method == 'POST':
        # Get the webhook URL and payload data from the form
        webhook_url = request.form['webhook_url']
        payload = request.form['payload']
        
        # Send the webhook request
        response = requests.post(webhook_url, data=payload, headers={'Content-Type': 'application/json'})
        
        # Check the response status code and return the result
        if response.status_code == 200:
            return jsonify({'status': 'success', 'message': 'Webhook sent successfully!'})
        else:
            return jsonify({'status': 'error', 'message': f'Webhook failed with status code: {response.status_code}'})

    return render_template('index.html')

if __name__ == '__main__':
  app.run(port=5000)
