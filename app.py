from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello(): 
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/predict')
def predict(): 
    return render_template('predict.html')

@app.route('/about')
def about(): 
    return render_template('about.html')
if(__name__ == '__main__'): 
    app.run(debug=True)