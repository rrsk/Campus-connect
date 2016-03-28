from flask import *
import urllib.request
import requests

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('home.html')

@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/freedata')
def free():
    return render_template('freedata.html')

@app.route('/contributors')
def contri():
    return render_template('contributors.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['input']
    x= str(text)
    f=0

    for i in range(len(x)):
        if(x[i]=='/'):
            f=i

    z=x[f+1:len(x)]

    urllib.request.urlretrieve(x,r'c:\python34\app\static\\'+z)
    return send_from_directory('static',z)

if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.103')
