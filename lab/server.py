from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/json")
def hello_json():
    return jsonify({"message": "hello world!"})
    # jsonifyを使うと、下記と同じコードがシンプルになる
    # data = {"message": "hello world!"}
    # response = Response(json.dumps(data), mimetype='application/json')
    # return response

@app.route("/no_content")
def no_content():
    return jsonify({"message": "No content found"}), 204

@app.route("/exp")
def exp():
    res = make_response("Hello world")
    res.status_code = 200
    return res

@app.route("/name_search")
def name_search():
    first_name = request.args.get("q")
    if not first_name:
        return jsonify({"message": "invalid parameter"}), 402
    for person in data:
        if person['first_name'] == first_name:
            return jsonify(person)    
    return jsonify({"message": "not found"}), 404

@app.route("/person/<string:id>", methods=["GET"])
def person(id):
    for person in data:
        if person['id'] == id:
            return jsonify(person)
    return jsonify({"message": "not found"}), 404

@app.route("/person/<string:id>", methods=["DELETE"])
def delete_person_by_id(id):
    for person in data:
        if person['id'] == id:
            return jsonify({"message": f"{id} is deleted."})
    return jsonify({"message": "not found"}), 404

@app.route("/person/<string:id>", methods=["POST"])
def add_person_by_id(id):
    req_data = request.json
    #print(req_data)
    return jsonify({"message": "success"})

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404


data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]
