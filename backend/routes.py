from flask import Blueprint, request, jsonify
from http import HTTPStatus

api = Blueprint('api', __name__)


@api.route('/calculate', methods=['POST'])
def calculate():
    try:
        person = request.get_json()
        # TODO: incluir variaveis restantes e descomentar
        age = validate_person(person)
        # person = Person(goal, name, age, weight, height)
        # wasted_daily, to_consume_daily = calculate_calories(person)
        # return jsonify(
        #     {
        #         "wasted_daily": wasted_daily,
        #         "to_consume_daily": to_consume_daily
        #     }), HTTPStatus.OK
        return jsonify({}), HTTPStatus.OK
    except ValueError as e:
        return jsonify({'Invalid data': str(e)}), HTTPStatus.BAD_REQUEST


def validate_person(person):

    def missing_property(prop):
        f'Missing {prop} property.'

    def invalid_property(prop):
        f'Invalid {prop} property.'

    if 'age' not in person:
        raise ValueError(missing_property('age'))

    age = person['age']
    if not isinstance(age, int):
        raise ValueError(invalid_property('age'))

    if not 0 < age < 126:
        raise ValueError('Age must be between 1 and 125. (inclusive)')

    # TODO: validar e retornar variaveis restantes
    # return goal, name, age, weight, height
    return age
