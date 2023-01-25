from flask import Flask ,jsonify
import inshort

app = Flask(__name__)

@app.route("/<string:lan>/<string:category>/")
def getData(lan,category):
    responce =  inshort.call(lan,category)
    return jsonify(responce)

@app.route("/")
def getDefaultData():
    responce = inshort.call('en', '')
    return jsonify(responce)

@app.route("/<string:lan>/")
def getDataOnLan(lan):
    responce = inshort.call(lan, '')
    return jsonify(responce)
    

app.run(debug=True)