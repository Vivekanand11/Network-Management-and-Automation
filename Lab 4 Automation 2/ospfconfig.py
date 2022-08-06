#!/ usr/bin/python3
from flask import Flask, render_template
from napalm import get_network_driver

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('Lab6main.html')
@app.route('/Get config')
def staticpage():
    return render_template('Get config.html', TargetRoute='/Get config',TargetPage='Home')
@app.route('/OSPF config')
def staticpage1():
    return render_template('OSPF config.html', TargetRoute='/OSPF config', TargetPage='Home')
@app.route('/Diff config')
def staticpage2():
    return render_template('Diff config.html', TargetRoute='/Diff config', TargetPage='Home')



if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1',port = 8080)