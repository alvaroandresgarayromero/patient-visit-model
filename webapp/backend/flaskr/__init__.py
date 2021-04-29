from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def health():
    return jsonify("Healthy!")


if __name__ == '__main__':
    app.run(host='0.0.0.0')