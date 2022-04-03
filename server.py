from flask import Flask,request,jsonify
import util
app=Flask(__name__)
@app.route("/")
def home():
    return "Welcome to Aashiyan"

@app.route("/locations")
def locations():
    response=jsonify({
        "locations":util.get_locations()
    })
    response.headers.add("Access-Control_Allow-Origin","*")

    return response
@app.route("/price",methods=["POST"])
def get_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    response=jsonify({
        "price":util.get_price(location,total_sqft,bhk,bath)
    })


    response.headers.add("Access-Control_Allow-Origin","*")

    return response







if __name__=="__main__":
    app.run(debug=True)