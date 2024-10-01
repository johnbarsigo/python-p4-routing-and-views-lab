#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index() :
    return '<h1>Python Operations with Flask Routing and Views<h1>'

@app.route('/print/<parameter>')
def print_string(parameter) :
    print (parameter)
    pass

@app.route('/count/<number>')
def count( number ) :
    for i in range ( number ) :
        print ( i, end="\n" )
    pass

@app.route('/math/<num1>/<operation>/<num2>')
def math( num1, operation, num2 ) :
    if (operation == '+') :
        return num1 + num2
    elif (operation == '-') :
        return num1 - num2
    elif (operation == '*') :
        return num1 * num2
    elif (operation == 'div') :
        return num1 / num2
    elif (operation == '%') :
        return num1 % num2


if __name__ == '__main__':
    app.run(port=5555, debug=True)
