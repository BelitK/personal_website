from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import datetime, time
from db import db, person


global switch, neg, qr_code
neg=True
switch=1
qr_code="0"

#make shots directory to save pics
person = person()


#instatiate flask app  
app = Flask(__name__)


camera = cv2.VideoCapture(-1, cv2.CAP_V4L)
qcd = cv2.QRCodeDetector()
db_con = db()


@app.route("/")
def home():
    return render_template("Homepage.html")


@app.route("/kommunity")
def kommunity():
    return render_template("Kommunity.html")


def gen_frames():  # generate frame by frame from camera
    global qr_code
    while True:
        success, frame = camera.read()
        if success:
            if neg:
                #frame=cv2.bitwise_not(frame) 
                retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(frame)
                # decc = decode(frame)
                if retval:
                    
                    frame= cv2.putText(frame,decoded_info[0], (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
                    if qr_code!= decoded_info[0]:
                        qr_code= decoded_info[0]
                else:
                    pass
                
            try:
                ret, buffer = cv2.imencode('.jpg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass


@app.route('/qr')
def index():
    return render_template('qr.html')

@app.route('/stream')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            time.sleep(1)
            if qr_code!=person.renum:
                person.renum=qr_code
                # print(person.renum)
                # print(person.token)
                print(f"info={person.renum}")
                person.token=db_con.get_token(qr_code)
                yield 'data: {}\n\n'.format(person.renum+" "+str(person.token))
            yield 'data: {}\n\n'.format(person.renum+" "+str(person.token))
    return Response(eventStream(), mimetype="text/event-stream")


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/requests',methods=['POST','GET'])
def tasks():
    global switch,camera
    if request.method == 'POST':
        if  request.form.get('neg') == 'Negative':
            global neg
            neg=not neg
        elif  request.form.get('stop') == 'Stop/Start':
            
            if(switch==1):
                switch=0
                camera.release()
                
            else:
                camera = cv2.VideoCapture(0)
                switch=1  
                 
    elif request.method=='GET':
        return render_template('qr.html',qr=qr_code)
    return render_template('qr.html',qr=qr_code)

@app.route('/token', methods = ['POST', 'GET'])
def token():
    if request.method == 'POST':
        form_data = request.form
        person.token = str(int(person.token)+int(form_data['textbox']))
        # embed()
        # print(form_data[0][2])
        db_con.update_token(person.renum, person.token)
        return redirect(url_for("tasks"))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="8000")

    
camera.release()