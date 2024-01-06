# Using flask to make an api
# import necessary libraries and functions
##################
from flask import Flask, jsonify, request
import subprocess
# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        print(request.method)

        data = "hello world"
        return jsonify({'data': data})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/push', methods = ['GET', 'POST', 'PUT'])
def disp():
    print(request.method)
    ##if request.method == 'POST' or 'PUT':
    
        ##data = (request.get_json())
        ##id = (data.get('id'))
        ##if id:
        ##    cmd = r"C:\Users\DK\Desktop\tamilboomi\feb-23\code\sample_poc\main.py --id {} --env {}".format(id, "dev")
        ##    subprocess.run('conda activate base && python {}'.format(cmd), shell=True)
        ##    #subprocess.Popen(cmd , shell=True)
    data = "hello welcome world"
    return jsonify({'data': data})

######
# driver function
if __name__ == '__main__':

    app.run(debug = True)