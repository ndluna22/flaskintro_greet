# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def oper_add():
    """Add a and b parameters."""

    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    return str(add(a, b))

@app.route('/sub')
def oper_sub():
    """Subtract and b parameters."""

    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    return str(sub(a, b))

@app.route('/mult')
def oper_mult():
    """Multiply a and b parameters."""

    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    return str(mult(a, b))

@app.route('/div')
def oper_div():
    """Divide a and b parameters."""

    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    return str(div(a, b))