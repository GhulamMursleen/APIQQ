import flask
from werkzeug.utils import secure_filename
from flask import  abort,request,send_file,jsonify, make_response
from model import Model
model=Model()

from flask_cors import CORS, cross_origin
app = flask.Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "API for Question Answer is working"
@app.route('/answer', methods = ['GET', 'POST'])
def append_file():
   json_data = flask.request.json
   if request.method == "OPTIONS": # CORS preflight
        return _build_cors_prelight_response()
   elif request.method == 'GET':
      #data = request.values
      print("coming",json_data["country"])
      if json_data["country"]!="":
          print(id,type(id))
          result,scores=model.startwork(json_data["question"],json_data["country"],int(json_data["mt"]),int(json_data["mr"]))
          return _corsify_actual_response(jsonify({"result":result,"Scores":scores}))
      else:
          return "error"
   else:
      return "error"
  

def _build_cors_prelight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    #response.headers.add('Access-Control-Allow-Headers', "*")
    #response.headers.add('Access-Control-Allow-Methods', "*")
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host= "0.0.0.0", port = 3000, threaded=True,debug=True, use_reloader=True)