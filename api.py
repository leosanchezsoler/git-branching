from flask import Flask, render_template
from src import covid_dash, hospitals_tb

<<<<<<< HEAD

=======
>>>>>>> 1f987ff3cf25893a20fdf09ec1e25919653eb9a8
app = Flask(__name__)
@app.route("/")
def landing_page():
 return render_template('index.html')
<<<<<<< HEAD
if __name__ == '__main__':
 app.run(host='0.0.0.0',port=1991, debug=True)

@app.route("/dashboard")
def dashboard():
 return render_template('dashboard.html')
@app.route("/map")
def map():
 return render_template('map.html')
=======

@app.route("/dashboard")
def dashboard():
 return render_template('dash.html')

@app.route("/map")
def map():
 return render_template('map.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=1991, debug=True)
>>>>>>> 1f987ff3cf25893a20fdf09ec1e25919653eb9a8
