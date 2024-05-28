import unittest
import json
from http import HTTPStatus
from app import create_app
from models import Goal, Gender, PhysicalActivity


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_calculate_should_return_ok(self):
        person = {
          "goal": Goal.GAIN_WEIGHT.value,
          "gender": Gender.MALE.value,
          "age": 21,
          "weightInKg": 86,
          "heightInCm": 186,
          "physicalActivity": PhysicalActivity.ACTIVE.value
        }

        response = self.client.post('/calculate', data=json.dumps(person), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('wasted_daily', response.get_data(as_text=True))
        self.assertIn('to_consume_daily', response.get_data(as_text=True))


    def test_calculate_should_return_bad_request_if_age_is_zero_or_less(self):
        person = {
          "goal": Goal.GAIN_WEIGHT.value,
            "gender": Gender.FEMALE.value,
            "age": 0,
            "weightInKg": 100,
            "heightInCm": 161,
            "physicalActivity": PhysicalActivity.SEDENTARY.value
        }

        response = self.client.post('/calculate', data=json.dumps(person), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_age_is_greater_than_125(self):
        person = {
          "goal": Goal.LOSE_WEIGHT.value,
          "gender": Gender.MALE.value,
          "age": 126,
          "weightInKg": 50,
          "heightInCm": 182,
          "physicalActivity": PhysicalActivity.SEDENTARY.value
        }

        response = self.client.post('/calculate', data=json.dumps(person), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_age_is_not_present(self):
        person = {
          "goal": Goal.MAINTAIN_WEIGHT.value,
          "gender": Gender.FEMALE.value,
          "weightInKg": 70,
          "heightInCm": 157,
          "physicalActivity": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=json.dumps(person), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_age_is_not_a_number(self):
        person = {
          "goal": Goal.MAINTAIN_WEIGHT.value,
          "gender": Gender.FEMALE.value,
          "age": "25 years",
          "weightInKg": 70,
          "heightInCm": 157,
          "physicalActivity": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=json.dumps(person), content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)


if __name__ == '__main__':
    unittest.main()
