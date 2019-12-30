#!/usr/bin/python

from flask import Flask, redirect , url_for
import isprime
import left
import right

app = Flask(__name__)

@app.route("/")

def hello():
    return "Hi, use /tsp/(your number) to check if it is a double sided prime number"

@app.route("/tsp/<i>")
def tspcheck(i):
    a = left.leftf(i)
    b = right.rightf(i)
    
    if (a and b):
        return 'True'
    else :
        return 'False'
    
    #print ('True') if a == b == True else  print ('False')
    #return


@app.route("/tsp/")
def tsp():
    return redirect(url_for("hello"))


if (__name__ == "__main__"):
    app.run(port = 8000, debug=True)
