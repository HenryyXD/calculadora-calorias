from flask import Blueprint, request, jsonify

api = Blueprint('api', __name__)

@api.route('/helloworld', methods=['GET'])
def helloworld(): 
    return "Hello World"
