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
            "objetivo": Goal.GAIN_WEIGHT.value,
            "sexo": Gender.MALE.value,
            "idade": 21,
            "peso": 86,
            "altura": 186,
            "exercicios": PhysicalActivity.ACTIVE.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.OK)


    def test_calculate_should_return_bad_request_if_age_is_zero_or_less(self):
        person = {
            "objetivo": Goal.GAIN_WEIGHT.value,
            "sexo": Gender.FEMALE.value,
            "idade": 0,
            "peso": 100,
            "altura": 161,
            "exercicio": PhysicalActivity.SEDENTARY.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_age_is_greater_than_125(self):
        person = {
          "objetivo": Goal.LOSE_WEIGHT.value,
          "sexo": Gender.MALE.value,
          "idade": 126,
          "peso": 50,
          "altura": 182,
          "exercicio": PhysicalActivity.SEDENTARY.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_age_is_not_present(self):
        person = {
          "objetivo": Goal.MAINTAIN_WEIGHT.value,
          "sexo": Gender.FEMALE.value,
          "peso": 70,
          "altura": 157,
          "exercicio": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_age_is_not_a_number(self):
        person = {
          "objetivo": Goal.MAINTAIN_WEIGHT.value,
          "sexo": Gender.FEMALE.value,
          "idade": "25 years",
          "peso": 70,
          "altura": 157,
          "exercicio": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_peso_is_not_present(self):
        person = {
            "objetivo": Goal.MAINTAIN_WEIGHT.value,
            "sexo": Gender.FEMALE.value,
            "idade": 25,
            "altura": 157,
            "exercicios": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_altura_is_not_present(self):
        person = {
            "objetivo": Goal.MAINTAIN_WEIGHT.value,
            "sexo": Gender.FEMALE.value,
            "idade": 25,
            "peso": 70,
            "exercicios": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_sexo_is_not_present(self):
        person = {
            "objetivo": Goal.MAINTAIN_WEIGHT.value,
            "idade": 25,
            "peso": 70,
            "altura": 157,
            "exercicios": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_objetivo_is_not_present(self):
        person = {
            "sexo": Gender.FEMALE.value,
            "idade": 25,
            "peso": 70,
            "altura": 157,
            "exercicios": PhysicalActivity.MODERATE.value
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_calculate_should_return_bad_request_if_exercicios_is_not_present(self):
        person = {
            "objetivo": Goal.MAINTAIN_WEIGHT.value,
            "sexo": Gender.FEMALE.value,
            "idade": 25,
            "peso": 70,
            "altura": 157
        }

        response = self.client.post('/calculate', data=person)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

if __name__ == '__main__':
    unittest.main()
