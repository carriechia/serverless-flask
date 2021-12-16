import requests
from config import Config

def get_sqs_message(event, context):
    config = Config()
    line_token = "{} {}".format("Bearer", config.LINE_TOKEN)

    for record in event['Records']:
        payload = record["body"]

        headers = {
        'Authorization': line_token,
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        r = requests.post('https://notify-api.line.me/api/notify',
                      headers=headers,
                      data={'message': 'Hello', 'body_message': str(payload)})