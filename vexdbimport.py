import json
from urllib.request import urlopen
# import requests

teamnum = input("Enter team number ")

# Matches
with urlopen(f'https://api.vexdb.io/v1/get_matches?team={teamnum}&season=Tower%20Takeover') as response:
    teams = response.read()

match_data = json.loads(teams)

print(json.dumps(match_data, indent=2))


# Rankings
with urlopen(f'https://api.vexdb.io/v1/get_rankings?team={teamnum}&season=Tower%20Takeover') as response:
    teams = response.read()

rank_data = json.loads(teams)

print(json.dumps(rank_data, indent=2))
