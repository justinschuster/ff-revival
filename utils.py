from espn_api.football import League

def fetch_league():
    '''
    fetch league data
    '''
    # league parameters
    league_id = '172893' 
    year = 2023

    # other auth info from devtools
    espn_swid = '{01041AA1-67E3-42CE-841A-A167E362CEB3}'
    espn_s2 = 'AEBxmAJt6Mcg44WhOALHUdh9n6GuzspKC8SymLGCiYU3Mk%2BZA0hew6uX8AKcQSXnWBT4j6cGoDgSqRjJFsS%2FyipBdXLC2Fz6QXFZK0KVt4moV%2FRdUXMBwbrGYzdHpxFqUQLhPlJBTNGAd74JWusLMrjlJl1uZUU%2BNu9fkjGTXrzbeMDJSrFhSXqZl0r4%2FI%2FJy3T3wRYFjRYuGhkcKNkXWe%2BBZz%2BnTa4tDlFpOkmbghgcW5TtGKZOOjn0r36Xuj4yzH2RKgxoZ0jzxAzeaNtC2J0FcKMdgpS6byEmTvKHkmYeOQ%3D%3D'

    # create url
    url = f'https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/leagueHistory/{league_id}?seasonId={year}'


    league = League(league_id=172893, year=2020, swid=espn_swid, espn_s2=espn_s2, debug=True)
    
    # set cookies
    league.cookies = {"swid": espn_swid, "espn_s2": espn_s2}
