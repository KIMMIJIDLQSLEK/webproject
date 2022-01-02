# from flask import Flask, render_template, request, jsonify
#
# app = Flask(__name__)
#
# from pymongo import MongoClient
#
# client = MongoClient('mongodb+srv://test:sparta@cluster0.nvsfa.mongodb.net/Cluster0?retryWrites=true&w=majority')
# db = client.dbsparta
#
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route("/bucket", methods=["POST"])
# def bucket_post():
#     bucket_receive = request.form['bucket_give']
#
#     bucket_list = list(db.bucket.find({}, {'_id': False}))
#     count = len(bucket_list) + 1
#
#     doc = {
#         'num': count,
#         'bucket': bucket_receive,
#         'done': 0
#     }
#     db.bucket.insert_one(doc)
#     return jsonify({'msg': '등록 완료'})
#
#
# @app.route("/bucket/done", methods=["POST"])
# def bucket_done():
#     num_receive = request.form['num_give']
#     db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
#     return jsonify({'msg': 'bucket 완료'})
#
#
# @app.route("/bucket", methods=["GET"])
# def bucket_get():
#     bucket_list = list(db.bucket.find({}, {'_id': False}))
#     return jsonify({'buckets': bucket_list})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)
#
# #############3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(기록) 연결 완료!'})


@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    sample_receive = request.form['sample_give']
    print(sample_receive)
    return jsonify({'msg': 'POST(완료) 연결 완료!'})


@app.route("/bucket", methods=["GET"])
def bucket_get():
    return jsonify({'msg': 'GET 연결 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
