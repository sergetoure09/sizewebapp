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
        if (result):
            try:
                msg_res=controler.send_data_email(email,size)
                if (msg_res):
                    return render_template("success.html",text="Email sent successfully to {0} ".format(email))  
                else:
                    return render_template("form.html",text="Error sending message to {0}".format(email))
            except Exception as e:
                print(e)         
        else:
            return render_template("form.html" ,
            text="Email already in database or verify the entry")

if __name__=="__main__":
    app.run(debug=True)