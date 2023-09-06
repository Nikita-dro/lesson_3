import requests
from flask import Flask, request, Response
from faker import Faker

fake = Faker()
app = Flask(__name__)


# 1
@app.get('/requirements')
def req():
    file = open('requirements.txt', 'r', encoding='utf-8')
    list_info = file.readlines()
    res = Response(''.join(list_info), content_type='text/plain')
    return res


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
    list_height = []
    list_weight = []
    for el in info[1:]:
        elem = el.strip('\n').split(',')
        if not len(elem) < 3:
            list_height.append(round(float(elem[1]) * 2.54, 2))
            list_weight.append(round(float(elem[2]) * 0.454, 2))
    result = (f'Average height - {round(sum(list_height) / len(list_height), 2)} cm'
              f'\nAverage weight - {round(sum(list_weight) / len(list_weight), 2)} kg')
    res = Response(result, content_type='text/plain')
    return res


# 4
@app.get("/space/")
def count_space():
    var = requests.get('http://api.open-notify.org/astros.json')
    return f'The number of cosmonauts at the current moment - {str(var.json()["number"])}'


if __name__ == "__main__":
    app.run()
