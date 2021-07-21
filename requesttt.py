from gevent import monkey

monkey.patch_ssl()

from requests import get
import requests

from csgo.client import CSGOClient
from steam.client import SteamClient

a = input("Identifier: ")


if a.startswith("7"):
    url = 'https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=9A65F9D44CB97F5C77860A705E15805A&steamid='
    steamid = str(a)  # change your steamID
    final_url = url + steamid
    r = requests.get(final_url).json()

    stats = {
        'total_kills': r['playerstats']['stats'][0]['value'],  # total kills
        'total_deaths': r['playerstats']['stats'][1]['value'],  # total deaths
        'total_time': r['playerstats']['stats'][2]['value']  # total time played
    }

    kd = stats['total_kills'] / stats['total_deaths']  # kill death ratio
    seconds_min = stats['total_time'] / 60  # seconds to minute
    hours = seconds_min / 60  # minute to hours
    kills = str(stats['total_kills'])  # kills
    deaths = str(stats['total_deaths'])  # deaths
    timeplayed = str("{:.2f}".format(hours))  # time played
    kdratio = str("{:.2f}".format(kd))  # Kill Death Ratio

    print("CS:GO Stats Notification - Executed!")

    print("Steam ID: " + steamid + " Total Kills: " + kills +
          " Total Deaths: " + deaths + " KDR: " + kdratio +
          " Time Played: " + timeplayed + " hours")
else:
    response = get('http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0002/?key=9A65F9D44CB97F5C77860A705E15805A&vanityurl=' + str(a))

    s = str(response.content)
    id = s[26:43]

    print(s)
    print(id)

    url = 'https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=730&key=9A65F9D44CB97F5C77860A705E15805A&steamid='
    steamid = str(id) #change your steamID
    final_url = url + steamid
    r = requests.get(final_url).json()

    stats = {
        'total_kills' : r['playerstats']['stats'][0]['value'], #total kills
        'total_deaths' : r['playerstats']['stats'][1]['value'], #total deaths
        'total_time' : r['playerstats']['stats'][2]['value'] #total time played
    }

    kd = stats['total_kills']/stats['total_deaths'] #kill death ratio
    seconds_min = stats['total_time']/60 # seconds to minute
    hours = seconds_min/60 #minute to hours
    kills = str(stats['total_kills']) #kills
    deaths = str(stats['total_deaths']) #deaths
    timeplayed = str("{:.2f}".format(hours)) #time played
    kdratio = str("{:.2f}".format(kd)) # Kill Death Ratio

    print("CS:GO Stats Notification - Executed!")

    print("Steam ID: " + steamid + " Total Kills: " + kills +
                   " Total Deaths: " + deaths + " KDR: " + kdratio +
                   " Time Played: " + timeplayed + " hours")