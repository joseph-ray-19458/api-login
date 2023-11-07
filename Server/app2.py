from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user', methods=['GET'])
def get_user_data():
    user_data = {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Joseph Ray",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
