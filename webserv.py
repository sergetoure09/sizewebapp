from flask import Flask,render_template,request
from control import *



app=Flask(__name__)
controler=controlers()

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/success/',methods=['POST'])
def success():
    if request.method=="POST":
        email=request.form["email_name"]
        size=request.form["size_name"]
        print(email,size)
        result=controler.record_entry_control(email,size)
        if(result):
            controler.send_data_email(email)
            return render_template("success.html")
            
        else:
            return render_template("form.html" ,
            text="Email already in database or verify the entry")

if __name__=="__main__":
    app.run(debug=True)