from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '8937091701:AAFDHJyv3qEQ10X8G09ukxQJGRtbwpa99_o'
CHAT_ID = '-1004408114916'


@app.route('/webhook', methods=['POST'])
def webhook():
  try:
    data = request.json
    message = data.get('text') or data.get('message', 'إشارة جديدة من المؤشر')

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message, 'parse_mode': 'Markdown'}
    requests.post(url, json=payload)

    return 'OK', 200
  except Exception as e:
    return str(e), 400


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
