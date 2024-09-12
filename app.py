from flask import Flask

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, World! Welcome to my Flask app."

if __name__ == '__main__':
    # Run the app on port 5001 (or any other port you want)
    app.run(debug=True, host='0.0.0.0', port=5001)

