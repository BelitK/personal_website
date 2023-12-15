import os
import time
from db import db, person
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for
import random
app = Flask(__name__)
db_con = db()
person = person()

# person.name=str(random.randint(0,10))
# person.renum=str(random.randint(0,10))
# person.token=str(random.randint(0,10))
# person.checkin='False'
# print(f"{'Isim = '+person.name+' Numara = '+person.renum+' Jeton = '+str(person.token)+' Checkin ='+person.checkin}")

@app.route("/")
def home():
    return render_template("Homepage.html")


@app.route("/kommunity")
def kommunity():
    return render_template("Kommunity.html")


@app.route('/qr')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_qr_code():
    data = request.get_json()
    content = data.get('qr_data', '')
    person.renum=content
    result = {"status": "success", "message": f"{'Isim = '+person.name+', Numara = '+person.renum+', Jeton = '+str(person.token)+', Checkin ='+person.checkin}","renum":person.renum}
    if person.oldrenum!=person.renum:
        #person.renum=qr_code
        # print(person.token)
        person.oldrenum=person.renum
        person.token, person.name, person.renum, person.checkin=db_con.get_token(person.renum)
        result = {"status": "success", "message": f"{'Isim = '+person.name+', Numara = '+person.renum+', Jeton = '+str(person.token)+', Checkin ='+person.checkin}","renum":f"{person.renum}"}
    print('get tokennn')
    print(person.renum)
    # Process the QR code content here (e.g., print or save it)
    #print(f"QR Code Content: {content}")

    return jsonify(result)

# @app.route('/stream')
# def stream():
#     def eventStream():
#         while True:
#             # wait for source data to be available, then push it
#             #print(f"info={person.renum}")
#             time.sleep(0.5)
#             if person.oldrenum!=person.renum:
#                 #person.renum=qr_code
#                 # print(person.token)
#                 person.renum=person.oldrenum
#                 person.token, person.name, person.renum=db_con.get_token(person.renum)
#                 print(person.renum)
#                 yield 'data: {}\n\n'.format(person.name+" "+person.renum+" "+str(person.token))
#             yield 'data: {}\n\n'.format(person.name+" "+person.renum+" "+str(person.token))
#     return Response(eventStream(), mimetype="text/event-stream")

# # SocketIO event handler for text broadcasting
# @socketio.on('broadcast_text')
# def handle_broadcast_text():
#     def eventStream():
#         while True:
#             # wait for source data to be available, then push it
#             #print(f"info={person.renum}")
#             time.sleep(0.5)
#             if person.oldrenum!=person.renum:
#                 #person.renum=qr_code
#                 # print(person.token)
#                 person.renum=person.oldrenum
#                 person.token, person.name, person.renum=db_con.get_token(person.renum)
#                 print(person.renum)
#                 yield 'data: {}\n\n'.format(person.name+" "+person.renum+" "+str(person.token))
#             yield 'data: {}\n\n'.format(person.name+" "+person.renum+" "+str(person.token))
#     print(f"Received message: {eventStream()}")
#     socketio.emit('display_text', eventStream(), broadcast=True)

@app.route('/token', methods = ['POST', 'GET'])
def token():
    if request.method == 'POST':
        form_data = request.form
        print('formdata::::')
        print(form_data['renum'])
        renum_num= form_data['renum']
        if form_data['token'] == '':
            return redirect(url_for("index"))
        tokenn = db_con.get_token(number=renum_num,just_token=True)
        person.token = str(int(tokenn)+int(form_data['token']))
        db_con.update_token(person.renum, person.token)
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="8000")
