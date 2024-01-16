from flask import Flask, jsonify, request
import json

application = app = Flask(__name__)

cars = [
    {
        'id': 0,
        'manufacturer': 'Ford',
        'model': 'Ford Bronco',
        'build': '1958'
    },
    {
        'id': 1,
        'manufacturer': 'Tesla',
        'model': 'T 258',
        'build': '2019'
    },
    {
        'id': 2,
        'manufacturer': 'Volvo',
        'model': 'Volvo C40',
        'build': '2000'
    },
    {
        'id': 3,
        'manufacturer': 'Volvo',
        'model': 'Volvo V60',
        'build': '2018'
    }
]


@app.route('/', methods=['GET'])
def home():
    return "Welcome to my API REST"


@app.route('/cars/', methods=['GET'])
def get_all_employees():
    """ Get all car collections
    :return: list of car
    :rtype: list
    """
    return jsonify(cars)


@app.route('/cars/<int:id>', methods=['GET'])
def get_employees_id(id: int):
    car = get_car_by_id(id)
    if car is None:
        return jsonify({
            'error': 'Employee does\'nt exist'
        }), 404
    return jsonify(car)


def get_car_by_id(id_car: int):
    """Get car with id mapping

    args:
    id_car(str): The id car

    Returns:
        dict: a dict with car representing given id
    """
    return next((car for car in cars if car['id'] == id_car), None)


def get_highest_id_car(cars_list: list) -> int:
    """ Get the highest id car within a collections of car
    :param cars_list: collections of dict
    :type cars_list: list
    :return: the highest id in collection
    :rtype: int
    """
    id_cars = []
    for car in cars_list:
        id_cars.append(car['id'])
    return max(id_cars)


@app.route('/cars', methods=['POST'])
def create_car():
    car = json.loads(request.data)
    car['id'] = get_highest_id_car(cars) + 1
    cars.append(car)
    return '', 201, {'location': f"/cars/{car['id']}"}


@app.route('/api/health', methods=['GET'])
def api_health():
    return jsonify({
        "status": "UP"
    })


if __name__ == '__main__':
    application.run(debug=False)

