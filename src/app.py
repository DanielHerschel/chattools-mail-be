from flask import Flask, request

from utils.configuration_manager import load_configutation

CONFIG = load_configutation()
app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
async def login():
    username = request.args.get("username")
    # TODO: Login the user.
    return {"status": "ok"}


@app.route("/send", methods=["GET", "POST"])
async def send_message():
    username = request.args.get("sendto")
    message = request.args.get("message")
    # TODO: Store the message in the DB.
    return {"status": "ok"}


@app.route("/inbox", methods=["GET", "POST"])
async def get_inbox():
    username = request.args.get("username")
    # TODO: Send all the messages in the inbox.
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host=CONFIG["api"]["host"], port=int(CONFIG["api"]["port"]))
