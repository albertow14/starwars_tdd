import unittest
import requests
from unittest.mock import MagicMock
import random

class ApiSwapi():
    def __init__(self, requests):
        self.requests = requests

    def get_total_count_of(self, people_or_planet):
        base_url = "https://swapi.co/api/"
        data = self.requests.get(f'{base_url}{people_or_planet}/')
        parsed_data = data.json()
        return parsed_data.get('count')
    
    def get_random_character(self):
        total_people = self.get_total_count_of('people')
        random_num = random.randint(1,total_people)
        data = self.requests.get(f"https://swapi.co/api/people/{random_num}/")
        data_json = data.json()
        return {"name": data_json.get('name'),
                "mass": data_json.get('mass'),
                "homeworld":data_json.get('homeworld')}
    
    def get_random_planet(self, person):
        planet_url_to_not_visit = person.get('homeworld')
        total_planets = self.get_total_count_of('planets')
        random_num = random.randint(1, total_planets)
        url = f'https://swapi.co/api/planets/{random_num}/'
        if url == planet_url_to_not_visit:
            self.get_random_planet(person)
        planet = self.requests.get(url)
        planet_data = planet.json()
        return {'name': planet_data.get('name'),
                'gravity': planet_data.get('gravity')}
        
    

####################################################################
def side_effect(value):
    fake_response = MagicMock()
    fake_response.json.return_value = {'name':'Luke', 'mass': 77, 'homeworld':'https://swapi.co/api/planets/20/', 'basura':'blablabla'}
    if value == 'https://swapi.co/api/people/' or value == 'https://swapi.co/api/planets/':        
        fake_response.json.return_value = {'count':87}
    elif 'https://swapi.co/api/planets/' in value:
        fake_response.json.return_value = {'name':'Naboo', 'gravity': 1}
    return fake_response


class TestCallApi(unittest.TestCase):
    def setUp(self):
        self.fake_request = MagicMock()
        self.fake_request.get = MagicMock(side_effect = side_effect)
        self.api_swapi = ApiSwapi(self.fake_request)

    def test_example_call_api_with_end_endpoint_people_return_persons(self):  

        expected_result = 87

        result = self.api_swapi.get_total_count_of('people')

        assert expected_result == result
        self.fake_request.get.assert_called_once_with('https://swapi.co/api/people/')
        

    def test_example_call_api_with_end_endpoint_people_return_planeta(self):
        expected_result = 87

        result = self.api_swapi.get_total_count_of('planets')

        assert expected_result == result
        self.fake_request.get.assert_called_once_with('https://swapi.co/api/planets/')

    def test_people_random_return_name_mass_planet(self):
        expected_result = {'name': 'Luke', 'mass': 77, 'homeworld':'https://swapi.co/api/planets/20/'}

        result = self.api_swapi.get_random_character()        
        
        assert result == expected_result

    def test_random_planet_except_homeworld_returns_name_and_gravity(self):
        expected_result = {'name':'Naboo', 'gravity': 1}
        person = self.api_swapi.get_random_character() 
        result = self.api_swapi.get_random_planet(person)

        assert result == expected_result

    def test_weight_in_random_planet(self):
        expected_result = f'Luke pesa 770 kg en su planeta natal y pesa 770 kg en Naboo .'
        
