from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://tmdgus5611:sparta@cluster0.2xqfo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/tensta_mypage", methods=["POST"])
def web_profile_post():
    img_receive = request.form['img_give']

    doc = {
        'img':img_receive
    }

    db.mars.insert_one(doc)
    return jsonify({'msg': '주문 완료!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)