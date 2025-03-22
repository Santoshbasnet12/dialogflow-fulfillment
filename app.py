# importing the required libraries
from flask import Flask, request, jsonify

# creating the flask app
app = Flask(__name__)

# this is the home route, when we open our website it shows my student number
@app.route('/')
def home():
    return jsonify({"student_number": "200581257"})

# this is the webhook route which Dialogflow will call to get the response
@app.route('/webhook', methods=['POST'])
def webhook():
    # getting the data sent by Dialogflow
    req = request.get_json()

    # checking which intent is triggered
    intent = req.get('queryResult').get('intent').get('displayName')

    # if the GetCryptoPrice intent is triggered, we send back this text
    if intent == "GetCryptoPrice":
        response_text = "The current Bitcoin price is $68,000!"
    else:
        response_text = "Sorry, I don't understand."

    # sending the response back to Dialogflow
    return jsonify({"fulfillmentText": response_text})

# running the flask app
if __name__ == '__main__':
    app.run(debug=True)
