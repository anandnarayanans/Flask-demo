from flask import Flask,render_template,flash


app=Flask(__name__)
app.secret_key="asddsf"

@app.route("/")
def index():
    flash("Hi Guyz")
    return render_template('index.html')


@app.route("/kaar",methods=['POST','GET'])
def greet():
    return 'Hi, How are you Dear Kaarian. Welcome to DigiVerz '
   
    


if __name__=="__main__":
    app.run(debug=True)