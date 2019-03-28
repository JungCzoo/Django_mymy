import os
import requests, json

params = {
    "api_key": 'RGAPI-c2d065f0-5b7c-41a8-b6bf-dad3524fa911',
}


def search(summoner_name):
    name = summoner_name
    response = requests.get('https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{0}'.format(name), params=params)
    summoner = response.json()
    id=summoner["id"]
    response_summoner = requests.get('https://kr.api.riotgames.com/lol/league/v4/positions/by-summoner/{0}'.format(id), params=params)
    summoner_dic = response_summoner.json()
    summoner_profile = []
    for k in summoner_dic:
        for j in k.values():
            summoner_profile.append(j)
    #랭크(4), 티어(5), 포인트(6),승(7),패(8),소환사이름(14)
    return summoner_profile
