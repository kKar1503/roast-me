from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>bruh</p>"

@app.get('/roast/<id>')
def roast_me(id):
    # Obtain the name parameter from the request
    name = request.args.get('name', '')

    # Generate a roast
    # Do something
    roast = f"Hello {name}, you are a bruh"

    # Return the roast
    return {
        "roast": roast,
    }