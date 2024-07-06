from robyn import Robyn

app = Robyn(__file__)


@app.get("/")
def index():
    return "Hello World - brian"


if __name__ == "__main__":
    app.start(host="127.0.0.1", port=8080)
