from flask import Flask # imported only Flask class from flask module, there are multiple classes available in flask module

app = Flask(__name__) # created Flask class instance with app name


@app.route('/') #we need route function to create path
def hello():
    return 'Hello, World!'

@app.route('/hello/')
def name():
    return 'vidya'

