from db import db, person
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file

app = Flask(__name__)
db_con = db()
person = person()


@app.route("/")
def home():
    return render_template("Homepage.html")


@app.route("/kommunity")
def kommunity():
    return render_template("Kommunity.html")


@app.route("/qr")
def index():
    return render_template("index.html")

@app.route('/kommunity/<id>')
def show_image(id):
    # Assuming your image is in the 'static' folder
    # ornek lal_pekin
    image_path = f'static/images/{id}.jpeg'

    # Specify the content type for the response (e.g., image/jpeg)
    content_type = 'image/jpeg'

    # Send the image file as a response
    try:
        return send_file(image_path, mimetype=content_type)
    except:
        return redirect(url_for('home'))

@app.route("/process", methods=["POST"])
def process_qr_code():
    data = request.get_json()
    content = data.get("qr_data", "")
    person.renum = content
    result = {
        "status": "success",
        "message": f"{'Isim = '+person.name+', Numara = '+person.renum+', Jeton = '+str(person.token)+', Checkin ='+person.checkin}",
        "renum": person.renum,
    }
    if person.oldrenum != person.renum:
        # person.renum=qr_code
        # print(person.token)
        person.oldrenum = person.renum
        person.token, person.name, person.renum, person.checkin = db_con.get_token(
            person.renum
        )
        result = {
            "status": "success",
            "message": f"{'Isim = '+person.name+', Numara = '+person.renum+', Jeton = '+str(person.token)+', Checkin ='+person.checkin}",
            "renum": f"{person.renum}",
        }
    # print('get tokennn')
    # print(person.token)
    # Process the QR code content here (e.g., print or save it)
    # print(f"QR Code Content: {content}")

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


@app.route("/token", methods=["POST", "GET"])
def token():
    if request.method == "POST":
        form_data = request.form
        # print('formdata::::')
        renum_num = form_data.get("renum")
        # print(form_data)
        if form_data["token"] == "":
            return redirect(url_for("index"))
        tokenn, numm = db_con.get_token(number=renum_num, just_token=True)
        tokenn = str(int(tokenn) + int(form_data["token"]))
        db_con.update_token(numm, tokenn)
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="8000")
