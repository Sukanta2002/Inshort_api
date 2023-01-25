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
    

if(__name__ =="__main__"):
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader =True)