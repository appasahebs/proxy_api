from flask import Flask, request, jsonify
from service.api_data_service import ApiDataService

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, OPTIONS"
    return response

@app.route('/')
def hello():
    return "Hello from OZY!"

@app.route('/ios')
def ios():
    return "Hello from ios OZY!"

@app.route("/ios/<string:endpoint>/")
def serve_endpoint(endpoint):
    return ApiDataService().getData(endpoint,request.args)

if __name__ == '__main__':
    app.run()

