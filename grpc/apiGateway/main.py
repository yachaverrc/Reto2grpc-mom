import os
from flask import Flask, jsonify
import grpc
import sys
sys.path.append('../')
import greeting_pb2
import greeting_pb2_grpc

app = Flask(__name__)

channel = grpc.insecure_channel('localhost:50051')
stub = greeting_pb2_grpc.FileServiceStub(channel)   


@app.route("/")
def hello():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = greeting_pb2_grpc.GreeterStub(channel)   
        response = stub.greet(greeting_pb2.ClientInput(greeting = "hola"))
        print("Greeter client received following from server: " + response.message)
    return response.message 

@app.route('/files', methods=['GET'])
def list_files():
    request = greeting_pb2.ListFilesRequest()
    response = greeting_pb2.ListFilesResponse(request)
    filenames = list(response.filenames)
    return jsonify(filenames)
    


if __name__ == '__main__':
    app.run(debug=True,port=4000)

