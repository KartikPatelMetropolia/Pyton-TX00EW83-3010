from flask import Flask, Response
import json

app = Flask(__name__)
@app.route('/prime_number/<number>')
def checkprime(number):
    i = 2
    number = int(number)
    while i < number:
        if number % i == 0:
            response = {
                "Number" : number,
                "isPrime" : False
            }
            return response
        i += 1
    response = {
        "Number" : number,
        "isPrime" : True
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)