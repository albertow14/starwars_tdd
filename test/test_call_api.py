import unittest
from unittest.mock import MagicMock

from ..api_swapi import ApiSwapi

{"name":"A planet", "gravity": "0.85 standard"}
{"name":"A planet", "gravity": "N/A"}    


def side_effect(value):
    fake_response = MagicMock()
    fake_response.json.return_value = {'name':'Luke', 'mass': "77", 'homeworld':'https://swapi.co/api/planets/20/', 'basura':'blablabla'}
    if value == 'https://swapi.co/api/people/' or value == 'https://swapi.co/api/planets/':        
        fake_response.json.return_value = {'count':"87"}
    elif 'https://swapi.co/api/planets/20/' == value:
        fake_response.json.return_value = {'name':'Naboo', 'gravity': "1 standard"}
    elif 'https://swapi.co/api/planets/' in value:
        fake_response.json.return_value = {'name':'Tierra', 'gravity': "1.5 (surface), 1 standard (Cloud City)"}
    return fake_response


class TestCallApi(unittest.TestCase):
    def setUp(self):
        self.fake_request = MagicMock()
        self.fake_request.get = MagicMock(side_effect = side_effect)
        self.api_swapi = ApiSwapi(self.fake_request)

    def test_example_call_api_with_end_endpoint_people_return_persons(self):  

        expected_result = "87"

        result = self.api_swapi.get_total_count_of('people')

        assert expected_result == result
        self.fake_request.get.assert_called_once_with('https://swapi.co/api/people/')
        

    def test_example_call_api_with_end_endpoint_people_return_planeta(self):
        expected_result = "87"

        result = self.api_swapi.get_total_count_of('planets')

        assert expected_result == result
        self.fake_request.get.assert_called_once_with('https://swapi.co/api/planets/')

    def test_people_random_return_name_mass_planet(self):
        expected_result = {'name': 'Luke', 'mass': "77", 'homeworld':'https://swapi.co/api/planets/20/'}

        result = self.api_swapi.get_random_character()        
        
        assert result == expected_result

    def test_random_planet_except_homeworld_returns_name_and_gravity(self):
        expected_result = {'name':'Tierra', 'gravity': '1.5 (surface), 1 standard (Cloud City)'}
        person = self.api_swapi.get_random_character() 
        result = self.api_swapi.get_random_planet(person)

        assert result == expected_result

    def test_result_happy_path(self):
        expected_result = 'Luke pesa 770.0 kg en Naboo y pesa 1155.0 kg en Tierra .'

        result = self.api_swapi.orchestator()

        assert result == expected_result

    def test_weight_in_random_planet_gravity_with_text(self):
        person = {"mass": "80"}
        planet = {"name":"A planet", "gravity": "N/A"}
        expected_result = 'Gravedad No conocida'

        result = self.api_swapi._get_kilos(person, planet)

        assert expected_result == result

    def test_weight_in_random_planet_gravity_with_text(self):
        person = {"mass": "80"}
        planet = {"name":"A planet", "gravity": "0.9 whatever"}
        expected_result = 720.0

        result = self.api_swapi._get_kilos(person, planet)

        assert expected_result == result



