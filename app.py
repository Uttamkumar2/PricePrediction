from flask import Flask,render_template,jsonify,request
import json
#from flask_cors import CORS

#import os 
#from flask import send_from_directory     

from pymongo import MongoClient 
from connections import cloudM_R
import os 

port = int(os.environ.get('PORT', 5000)) 
#app.run(host='0.0.0.0', port=port)


app=Flask(__name__)
#CORS(app)


@app.route("/")
def home():

    
    return render_template('index.html')

@app.route("/readData")
def read():
        altdatadf = cloudM_R()
        #resdf=altdatadf[(altdatadf["Year"]==2019)]
        resdf=altdatadf
        return jsonify(resdf.to_dict('records'))

#@app.route('/favicon') 
#def favicon(): 
#    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.ico')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__=='__main__':
    #app.run(host='0.0.0.0', port=port)
    app.run(debug=True)