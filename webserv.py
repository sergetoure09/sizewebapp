from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/success/',methods=['POST'])
def success():
    return render_template("success.html")

if __name__=="__main__":
    app.run(debug=True)