Alexa Messenger
================

There isn't yet a good way to send text messages using Alexa, a feature I think would be a great addition.
So that's what this is, an Alexa app that hooks into Google's Oauth to grab contact data, and sends texts out using Twilio.

Under Development
-----------

This is an incomplete Python app built in Flask for Amazon's Alexa.
The code is not yet organized, and I'm still working on Account Linking with Google.

Plug in some Twilio creds and it will send texts to whatever number you hard code.

Setup
================

Better, more detailed instructions coming soon..

In the Interaction Model section of the Amazon Developer Console's Skill page:
* paste the contents of ./resources/intent_schema.json to the first text area
* paste the contents of ./resources/sample_utterances.txt to the second text area

This app only runs on https, you may want to use a tool like Ngrok to host the client on your local environment. If you ran the app using **python send_message.py** then the app is now running locally on port **5000**, and you should run Ngrok using: **./ngrok http 5000** in whichever folder you've set up ngrok in.