import os
from flask import url_for, Flask, request, render_template, redirect, make_response
from printd import printd
from printrun.printcore import printcore
import time

app = Flask(__name__)

@app.route('/')
def home():
    os.system('rm static/monfichier.jpg')
    os.system('fswebcam -r 640x480 --jpeg 100 -D 0.1 static/monfichier.jpg')
    return render_template('index.html')


@app.route('/rimg')
def test():
    os.system('rm static/monfichier.jpg')
    os.system('fswebcam -r 640x480 --jpeg 85 -D 0.1 static/monfichier.jpg')
    return url_for('home')


@app.route('/info')
def style():
    return str(os.popen("vcgencmd measure_temp").read())

@app.route('/shutdownSite')
def shutdownSite():
    os.system('kill -9 $(sudo lsof -t -i:20078)')
    return 404

@app.route('/stopprint')
def stopPrint():
    p=printcore('/dev/ttyUSB0', 115200)
    while not p.online:
        time.sleep(0.1)
    p.pause()
    p.send_now("G1 X25 Y260")#present
    p.send_now("M106 S0")#fan off
    p.send_now("M104 S0")#hotend off
    p.send_now("M140 S0")#bed off
    p.send_now("G1 Z10")#raise Z
    p.disconnect()

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        f=request.files['file']
        toprint = f.filename
        f.save('toprint.gcode')
    print('toprint.gcode')
    return redirect('/')

@app.route('/pprint')
def moustique():#merci louison
    print("starting printing ...")
    printd('toprint.gcode')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=20078)
