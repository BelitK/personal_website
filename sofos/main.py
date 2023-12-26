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

@app.route("/davetliler")
def davetli():
    data = db_con.fetchh()
    return render_template("shwall.html", veri =data)

@app.route("/kommunity/<id>")
def show_image(id):
    # Assuming your image is in the 'static' folder
    # ornek lal_pekin
    image_path = f"static/images/{id}.jpeg"

    # Specify the content type for the response (e.g., image/jpeg)
    content_type = "image/jpeg"

    # Send the image file as a response
    try:
        return send_file(image_path, mimetype=content_type)
    except:
        return redirect(url_for("home"))


@app.route("/kommunity/hamson")
def show_pdf():
    # Assuming your image is in the 'static' folder
    # ornek lal_pekin
    image_path = "static/images/Hamson.pdf"

    # Send the image file as a response
    try:
        return send_file(image_path)
    except:
        return redirect(url_for("home"))


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


@app.route("/new_in")
@app.route("/new_in/<name>")
@app.route("/new_in/<name>&<Kaydeden>&<id>")
def add_in(name="None", Kaydeden="None", id="None"):
    print(name, Kaydeden, id)

    return render_template("new_in.html", name=name, kaydet=Kaydeden, id=id)


@app.route("/new_invite", methods=["POST", "GET"])
def add_invite():
    if request.method == "POST":
        form_data = request.form
        # print('formdata::::')
        isim = form_data.get("isim")
        kaydeden = form_data.get("kaydeden")
        print(form_data)
        if isim == "":
            return redirect(url_for("add_in", name="bos giris yapma"))
        id = db_con.insert_new(name=isim, ekleyen=kaydeden)
        print(id)
        # print(form_data)
        # if form_data["token"] == "":
        #     return redirect(url_for("add_in",name=isim, Kaydeden=kaydeden))
        return redirect(url_for("add_in", name=isim, Kaydeden=kaydeden, id=id))
    return redirect(url_for("add_in"))


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
        person.oldrenum = ""
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="8000")
