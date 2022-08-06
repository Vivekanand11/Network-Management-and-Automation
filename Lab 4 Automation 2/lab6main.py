#!/ usr/bin/python3
from flask import Flask, render_template, request
from prettytable import PrettyTable

app = Flask(__name__)   
@app.route('/')
def index():
    return render_template('Lab6main.html')
@app.route('/Get config')
def staticpage():
    return render_template('getconfig.html', TargetRoute='/Get config',TargetPage='Home')
@app.route('/OSPF config', methods = ["GET", "POST"])
def staticpage1():
    if request.method == "POST":
       Vivek=request.form.get("username")
       Vaibhav=request.form.get("password")
       ospf_area_id=request.form.get("area id")
       ospf_process_id=request.form.get("process id")
       loopback1=request.form.get("loopback")
       return "SSH credentials are "+Vivek+','+Vaibhav+', '+ospf_area_id+', '+ospf_process_id+','+loopback1

    return render_template('R1.html', TargetRoute='/OSPF config', TargetPage='Home')
@app.route('/Diff config')
def staticpage2():
    return render_template('Diff config.html', TargetRoute='/Diff config', TargetPage='Home')



if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.3',port = 8080)