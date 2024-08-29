import json
import requests
import pandas as pd 

# league parameters
league_id = '172893' 
year = 2023

# other auth info from devtools
espn_swid = '{01041AA1-67E3-42CE-841A-A167E362CEB3}'
espn_s2 = 'AEBxmAJt6Mcg44WhOALHUdh9n6GuzspKC8SymLGCiYU3Mk%2BZA0hew6uX8AKcQSXnWBT4j6cGoDgSqRjJFsS%2FyipBdXLC2Fz6QXFZK0KVt4moV%2FRdUXMBwbrGYzdHpxFqUQLhPlJBTNGAd74JWusLMrjlJl1uZUU%2BNu9fkjGTXrzbeMDJSrFhSXqZl0r4%2FI%2FJy3T3wRYFjRYuGhkcKNkXWe%2BBZz%2BnTa4tDlFpOkmbghgcW5TtGKZOOjn0r36Xuj4yzH2RKgxoZ0jzxAzeaNtC2J0FcKMdgpS6byEmTvKHkmYeOQ%3D%3D'

# create url
url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{league_id}?seasonId={year}'

class League:
    '''
    Class of ESPN Fantasy Football League
    '''
    # create url
    def __init__(self, league_id, year, swid, espn_s2):
        self.league_id = league_id
        self.year = year
        self.swid = espn_swid
        self.espn_s2 = espn_s2
        self.owners = []
        self.url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{self.league_id}?seasonId={self.year}'
        self.cookies = {
            "swid": self.swid,
            "espn_s2": self.espn_s2
        }

    def make_request(self):
        resp = requests.get(self.url, cookies={"swid": self.swid, "espn_s2": self.espn_s2})
        return resp

    def get_owners(self):
        resp = self.make_request()
        body = json.loads(resp.text)[0]
        print(body)
        for owner in body["members"]:
            self.owners.append(owner['displayName'])

    def check_other_stuff(self):
        resp = self.make_request()
        body = json.loads(resp.text)[0]

if __name__ == "__main__":
    league = League(league_id, year, espn_swid, espn_s2)
    league.get_owners()
    league.check_other_stuff()
