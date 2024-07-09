#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index ():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string ( parameter ):
    print ( f"{parameter}" )
    return f'<h1>{parameter}</h1>'

@app.route('/count/<int:parameter>')
def count( parameter ) :
    for i in range (1, parameter) :
        return ( f'{i}\n' )
    # numbers = range (0, counter + 1)
    # # for i in numbers :
    # #     return f'{i}\n'
    # numbers_html = '<br>'.join(str(number) for number in numbers)
    # return f'<p>{numbers_html}</p>'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math (num1, operation, num2) :
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<p>Error: Division by zero</p>'
    elif operation == '%':
        result = num1 % num2
    else:
        return '<p>Error: Unsupported operation</p>'
    return f'<p>{num1} {operation} {num2} = {result}</p>'

@app.route('/print/<string:text>')
def print_text( text ):
    print (text)
    return text


if __name__ == '__main__':
    app.run(port=5555, debug=True)
