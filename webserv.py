from flask import Flask,render_template,request
from control import *

controler = controlers()

app=Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/success/',methods=['POST'])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        size=request.form["size_name"]
        controler.record_entry_control(email,size)
    return render_template("success.html")

if __name__=="__main__":
    app.run(debug=True)