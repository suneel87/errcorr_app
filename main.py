from flask import Flask
from flask import render_template, request, jsonify
from app import views
from app.views import genderapp
from app.med_corr import predict

app = Flask(__name__) # webserver gateway interphase (WSGI)

@app.route('/process_input', methods=['GET', 'POST'])
def process_input():
    input_string = request.form['input']
    output_string = predict(input_string)
    return output_string

app.add_url_rule(rule='/',endpoint='home',view_func=views.index)
app.add_url_rule(rule='/app/',endpoint='app',view_func=views.app)
app.add_url_rule(rule='/app/gender/',
                 endpoint='gender',
                 view_func=views.genderapp,
                 methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True)