from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "欢迎来到剧本家游戏服务器"})

@app.route("/user/<username>")
def get_user(username):
    return jsonify({"username": username, "status": "在线"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)