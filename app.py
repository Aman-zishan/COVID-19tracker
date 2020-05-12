from flask import Flask, render_template, url_for,request, redirect, jsonify
import COVID19Py, requests, json


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/updates', methods=["GET", "POST"])
def updates():
        option = request.form['op']
        covid19 = COVID19Py.COVID19(data_source="nyt")
        location = covid19.getLocationByCountryCode({option})
        location_user = json.dumps(location)
        data = json.loads(location_user)
        return render_template("result.html",data = data )
        
        

        
if __name__ == "__main__": 
        app.run(debug=True)