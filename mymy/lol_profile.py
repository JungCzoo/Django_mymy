# import os
# import requests, json
#
#
# params = {
#     "api_key": 'RGAPI-ca77a306-c9b6-4199-ba5d-4933b43514e9',
# }
#
#
# def search():
#     response = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{0}'.format(name), params=params)
#     summoner = response.json()
#     id=summoner["id"]
#
#     response_summoner = requests.get('https://kr.api.riotgames.com/lol/league/v4/positions/by-summoner/{0}'.format(id), params=params)
#     summoner_profile = response_summoner.json()
#
#
