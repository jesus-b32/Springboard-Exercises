# Put your app in here.
import operations
from flask import Flask, request
app = Flask(__name__)

@app.route('/add')
def calc_add():
    """Add a and b parameters..
    For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.
    """

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.add(a, b)

    return str(result)


@app.route('/sub')
def calc_sub():
    """Subtract a and b parameters.."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.sub(a, b)

    return str(result)



@app.route('/mult')
def calc_mult():
    """Multiply a and b parameters.."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.mult(a, b)

    return str(result)



@app.route('/div')
def calc_div():
    """Divide a and b parameters.."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations.div(a, b)

    return str(result)




operators = {
        "add": operations.add,
        "sub": operations.sub,
        "mult": operations.mult,
        "div": operations.div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
