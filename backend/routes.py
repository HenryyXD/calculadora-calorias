from flask import Blueprint, render_template, request, jsonify
from http import HTTPStatus
from models import Person, Goal, Gender, PhysicalActivity
from services import calculate_calories

api = Blueprint('api', __name__)


@api.route('/calculate', methods=['POST'])
def calculate():
    try:
        person_data = request.form.to_dict()
        
        goal = Goal[person_data.get('objetivo').upper()]
        gender = Gender[person_data.get('sexo').upper()]
        age = int(person_data.get('idade'))
        weightInKg = float(person_data.get('peso'))
        heightInCm = float(person_data.get('altura'))
        physicalActivity = PhysicalActivity[person_data.get('exercicios').upper()]

        person = Person(
            goal=goal,
            gender=gender,
            age=age,
            weightInKg=weightInKg,
            heightInCm=heightInCm,
            physicalActivity=physicalActivity
        )

        wasted_daily, to_consume_daily = calculate_calories(person)
        return render_template('results.html', wasted_daily=wasted_daily, to_consume_daily=to_consume_daily)
    except ValueError as e:
        return render_template('error.html', mensagem=str(e))


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
