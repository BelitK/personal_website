import time
from db import db, person
from flask import Flask, render_template, request, jsonify, Response, redirect, url_for

app = Flask(__name__)
db_con = db()
person = person()

global qr_code
qr_code = '0'

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
    global qr_code
    data = request.get_json()
    content = data.get('content', '')
    qr_code=content
    # Process the QR code content here (e.g., print or save it)
    print(f"QR Code Content: {content}")
    return jsonify({'status': 'success'})

@app.route('/stream')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            #print(f"info={person.renum}")
            time.sleep(0.5)
            if qr_code!=person.renum:
                #person.renum=qr_code
                # print(person.token)
                person.token, person.name, person.renum=db_con.get_token(qr_code)
                print(person.renum)
                yield 'data: {}\n\n'.format(person.name+" "+person.renum+" "+str(person.token))
            yield 'data: {}\n\n'.format(person.name+" "+person.renum+" "+str(person.token))
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/token', methods = ['POST', 'GET'])
def token():
    if request.method == 'POST':
        form_data = request.form
        person.token = str(int(person.token)+int(form_data['textbox']))
        # embed()
        # print(form_data[0][2])
        db_con.update_token(person.renum, person.token)
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="8000")
