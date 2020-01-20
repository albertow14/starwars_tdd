import unittest
import requests
from unittest.mock import MagicMock

class ApiSwapi():
    def __init__(self, requests):
        self.requests = requests

    def get_total_count_of(self, people_or_planet):
        base_url = "https://swapi.co/api/"
        data = self.requests.get(f'{base_url}{people_or_planet}')
        parsed_data = data.json()
        return parsed_data.get('count')
    



class TestCallApi(unittest.TestCase):
    def setUp(self):
        self.fake_json = MagicMock()
        self.fake_request = MagicMock()
        self.fake_request.get.return_value = self.fake_json
        self.api_swapi = ApiSwapi(self.fake_request)

    def test_example_call_api_with_end_endpoint_people_return_persons(self):
        fake_result = {'count':87}        
        self.fake_json.json.return_value = fake_result             

        expected_result = 87

        result = self.api_swapi.get_total_count_of('people')

        assert expected_result == result
        self.fake_request.get.assert_called_once_with('https://swapi.co/api/people')
        

    def test_example_call_api_with_end_endpoint_people_return_planeta(self):
        fake_result = {'count':1}
        self.fake_json.json.return_value = fake_result

        expected_result = 1

        result = self.api_swapi.get_total_count_of('planets')

        assert expected_result == result
        self.fake_request.get.assert_called_once_with('https://swapi.co/api/planets')

    def test_people_random_return_name_mass_planet(self):
        assert False