from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "欢迎来到游戏服务器"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)