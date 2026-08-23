from flask import Flask, jsonify

# Elastic Beanstalk's Python platform looks for a variable named "application"
application = Flask(__name__)

@application.route("/")
def home():
    return "Hello from my Flask app on Elastic Beanstalk!"

@application.route("/health")
def health():
    return jsonify({"status": "ok"})

@application.route("/greet/<name>")
def greet(name):
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    application.run(debug=True)