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
        planet = self._get_planet_data(url)        
        return {'name': planet.get('name'),
                'gravity': planet.get('gravity')}
            
    def orchestator(self):
        person = self.get_random_character()        
        homeworld = self._get_planet_data(person.get('homeworld'))
        planet_to_visit = self.get_random_planet(person)    
        kilos_homeworld = self._get_kilos(person, homeworld)                  
        kilos_planet_visited = self._get_kilos(person, planet_to_visit)       
        return f'{person.get("name")} pesa {kilos_homeworld} kg en {homeworld.get("name")} y pesa {kilos_planet_visited} kg en {planet_to_visit.get("name")} .'

    def _get_kilos(self, person, planet):
        planet_gravity = planet.get('gravity')
        try:
            int(planet_gravity[0])
        except ValueError:
            return 'Gravedad No conocida'
        if len(planet_gravity) > 1:
            if planet_gravity[1] == '.':
                planet_gravity = planet_gravity[:3]
            else:
                planet_gravity = planet_gravity[0]
        planet_gravity = float(planet_gravity)
        mass_string = person.get('mass')
        persona_peso = mass_string.replace(",",".")
        try:      
            return float(persona_peso) * float(planet_gravity) * float(10)
        except ValueError:
            return 'Masa no conocida'

    def _get_planet_data(self, planet_url):
        planet = self.requests.get(planet_url)
        return planet.json()