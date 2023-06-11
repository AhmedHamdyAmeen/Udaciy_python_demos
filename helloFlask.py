from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate Our Application:
app = Flask(__name__)

# Routes:


@app.route('/')
def hello():
    return f'Hello, World'


# always include this at the bottom of your code to run the Flask App Automatically.
if __name__ == '__main__':
    app.run(host="0.0.0.0")


'''
To Run the Flask app:
FLASK_APP=NameOfYourApp.py flask run
FLASK_APP=app.py FLASK_DEBUG=true flask run

@app.route is a Python decorator. Decorators take functions and returns another function


'''
