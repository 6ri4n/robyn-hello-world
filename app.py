from robyn import Robyn
from dotenv import load_dotenv
import os

app = Robyn(__file__)
load_dotenv()
port = os.getenv("PORT") or 8080

@app.get("/")
def index():
    return "Hello World - brian"


if __name__ == "__main__":
    app.start(host="0.0.0.0", port=port)
