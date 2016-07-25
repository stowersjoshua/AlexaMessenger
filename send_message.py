
import logging

from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
from twilio.rest import TwilioRestClient

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

ACCOUNT_SID = 'Twilio Account ID'
AUTH_TOKEN = 'Twilio Auth Token'


class Message(object):
    def __init__(self):
        self.receiver = None
        self.message_body = None

message = Message()


@ask.intent('BeginIntent')
def begin(contact):
    message.receiver = contact
    response_text = render_template('request_message', name=contact)
    help_text = render_template('help')
    return question(response_text).reprompt(help_text)


@ask.intent('RequestMessageBodyIntent')
def request_message_body(message_body):
    message.message_body = message_body

    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        to = '2105553998',
        from_ = '2105551244',
        body = "Message: " + message.message_body
    )

    
    response_text = render_template('request_body', message_body=message_body)
    return question(response_text)


@ask.intent('AMAZON.StopIntent')
def stop():
    text = render_template('stop')
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.session_ended
def session_ended():
    return "", 200


if __name__ == '__main__':

    app.run(debug=True)
