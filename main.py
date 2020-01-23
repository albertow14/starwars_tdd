import requests
from api_swapi import ApiSwapi


api = ApiSwapi(requests)
result = api.orchestator()
print(result)