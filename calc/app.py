# Put your app in here.
from flask import Flask, request
import operations 

app = Flask(__name__)

@app.route('/add')
def add():
    """Adds a and b and returns result as the body."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.add(a, b))

@app.route('/sub')
def sub():
    """Subtracts b from a and returns result as the body."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.sub(a, b))

@app.route('/mult')
def mult():
    """Multiplies a and b and returns result as the body."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.mult(a, b))

@app.route('/div')
def div():
    """Divides a by b and returns result as the body."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(operations.div(a, b))