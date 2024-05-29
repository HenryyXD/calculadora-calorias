from flask import Blueprint, render_template, request, jsonify
from http import HTTPStatus
from models import Person, Goal, Gender, PhysicalActivity
from services import calculate_calories

api = Blueprint('api', __name__)


@api.route('/calculate', methods=['POST'])
def calculate():
    try:
        person_data = request.form.to_dict()
        errors = validate(person_data)

        if errors:
            return jsonify({"erros": errors}), HTTPStatus.BAD_REQUEST

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
        return render_template('results.html', wasted_daily=wasted_daily, to_consume_daily=to_consume_daily), HTTPStatus.OK
    except Exception as e:
        return jsonify({"erro": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR


def __missing_property(prop):
    return f'Campo {prop} ausente.'

def __invalid_property(prop):
    return f'Valor de {prop} invalido.'

def validate(person):
    errors = []
    errors.extend(validate_age(person))
    errors.extend(validate_weight(person))
    errors.extend(validate_height(person))
    errors.extend(validate_gender(person))
    errors.extend(validate_goal(person))
    errors.extend(validate_physical_activity(person))
    return errors

def validate_age(person):
    errors = []
    if 'idade' not in person:
        errors.append(__missing_property('idade'))
    else:
        age = person['idade']
        if not age.isdigit():
            errors.append(__invalid_property('idade'))
        else:
            age = int(age)
            if not 0 < age < 126:
                errors.append('Idade tem que estar entre 1 e 125.')
    return errors

def validate_weight(person):
    errors = []
    if 'peso' not in person:
        errors.append(__missing_property('peso'))
    else:
        weight = person['peso']
        try:
            weight = float(weight)
        except ValueError:
            errors.append(__invalid_property('peso'))
        else:
            if not 0 < weight < 400:
                errors.append('Peso deve ser um numero positivo menor que 400 kg.')
    return errors

def validate_height(person):
    errors = []
    if 'altura' not in person:
        errors.append(__missing_property('altura'))
    else:
        height = person['altura']
        try:
            height = float(height)
        except ValueError:
            errors.append(__invalid_property('altura'))
        else:
            if not 50 < height < 250:
                errors.append('Altura deve estar entre 50 cm e 250 cm.')
    return errors

def validate_gender(person):
    errors = []
    if 'sexo' not in person:
        errors.append(__missing_property('sexo'))
    else:
        gender = person['sexo']
        if gender.upper() not in Gender.__members__:
            errors.append(__invalid_property('sexo'))
    return errors

def validate_goal(person):
    errors = []
    if 'objetivo' not in person:
        errors.append(__missing_property('objetivo'))
    else:
        goal = person['objetivo']
        if goal.upper() not in Goal.__members__:
            errors.append(__invalid_property('objetivo'))
    return errors

def validate_physical_activity(person):
    errors = []
    if 'exercicios' not in person:
        errors.append(__missing_property('exercicios'))
    else:
        physical_activity = person['exercicios']
        if physical_activity.upper() not in PhysicalActivity.__members__:
            errors.append(__invalid_property('exercicios'))
    return errors