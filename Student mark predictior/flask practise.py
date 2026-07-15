from flask import Flask

# Create a Flask application

app = Flask(__name__)

# Home route
# "Whenever someone visits the home URL (/), execute the function below."
@app.route('/')
def index():
    return 'WELCOME TO FLASK DEPLOYMENT'


# Run the application

#app.run(host='0.0.0.0', port=81)

app.run(host = '127.0.0.1', port=5000)

