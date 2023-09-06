import requests
from flask import Flask, request, Response
from faker import Faker

fake = Faker()
app = Flask(__name__)


# 2
@app.get("/generate-users/")
def generate():
    query = request.args.get('num_users', default=100, type=int)
    if query > 0:
        list_users = []
        for i in range(query):
            list_users.append(f'{fake.name()}, {fake.email()}')
        info = '\n'.join(list_users)
        res = Response(info, content_type='text/plain')
        return res
    else:
        return 'num_users must be greater than 0'


# 3
@app.get('/mean/')
def mean():
    file = open('hw.csv', 'r', encoding='utf-8')
    info = file.readlines()
    list_res = []
    for el in info[1:]:
        elem = el.strip('\n').split(',')
        if not len(elem) < 3:
            list_res.append(f'Index - {elem[0]}, height - {round(float(elem[1]) * 2.54, 2)},'
                            f' weight - {round(float(elem[2]) * 0.454, 2)}')
    res = Response('\n'.join(list_res), content_type='text/plain')
    return res


# 4
@app.get("/space/")
def count_space():
    var = requests.get('http://api.open-notify.org/astros.json')
    return f'The number of cosmonauts at the current moment - {str(var.json()["number"])}'


if __name__ == "__main__":
    app.run()
