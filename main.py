import requests
from flask import Flask

app = Flask(__name__)


# 4
@app.get("/space/")
def count_space():
    var = requests.get('http://api.open-notify.org/astros.json')
    return f'The number of cosmonauts at the current moment - {str(var.json()["number"])}'


if __name__ == "__main__":
    app.run()