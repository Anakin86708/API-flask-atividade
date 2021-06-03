from settings import Settings
from flask import Flask, request, jsonify

app = Flask(__name__)
app.run(host="0.0.0.0")

index = 0

def next_index():
    global index
    index +=1
    return index

def result(message: str):
    return {'result': message}

data = {}

@app.route('/', methods = ['GET'])
def initial():
    return 'Hello'

@app.route('/data', methods = ['GET'])
def get_data():
    return {k:v.as_json() for k, v in data.items()}

@app.route('/data/<id>', methods = ['GET'])
def get_data_from(id):
    try:
        return data[int(id)].as_json()
    except KeyError:
        return result(f'KeyError: {id}')

@app.route('/data', methods = ['POST'])
def set_data():
    data[next_index()] = Settings(request.form['eventNotificationsState'], request.form['onlyFavoriteState'], request.form['updateFrequencyValue'])
    return result('ok')

@app.route('/data/<id>', methods = ['PUT'])
def update_data(id):
    data[int(id)] = Settings(request.get_json()['eventNotificationsState'], request.get_json()['onlyFavoriteState'], request.get_json()['updateFrequencyValue'])
    print('Recived data:', data[int(id)])
    return result('ok')

@app.route('/data/<id>', methods = ['DELETE'])
def delete_data(id):
    data.pop(int(id))
    return result('ok')
