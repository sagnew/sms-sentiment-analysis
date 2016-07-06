import json

from flask import Flask, request
from twilio import twiml

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms_reply():
    add_ons = json.loads(request.form['AddOns'])
    if add_ons['status'] == 'successful':
        result = add_ons['results']['ibm_watson_sentiment']['result']
        sentiment = result['docSentiment']['type']
        response_message = 'Your response was {}.'.format(sentiment)
    else:
        response_message = 'An error has occured.'

    response = twiml.Response()
    response.message(response_message)
    return str(response)

app.run()
