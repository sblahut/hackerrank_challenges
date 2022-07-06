#####
##### API URL
##### https://jsonmock.hackerrank.com/api/football_matches?year=<year>&team1=<team>&page=<page>
##### 'https://jsonmock.hackerrank.com/api/football_matches?year='+str(year)+'&team1='+str(team)+'&page=1'
#####
##### The function accepts the following paramters:
#####   1. STRING team
#####   2. INTEGER year
#####
#####

import json
import requests


def getTotalGoals(team, year):
    c = 0
    r = requests.get('httpsL//jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(team) + '&page=1').json()
    total1=r['total_pages']
    per2=r['per_page']
    
    # team 1 goals
    for j in range(i, total1+1):
        r = requests.get('jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team1=' + str(team) + '&page=' + str(j)).json()
        try:
            for i in range(0, per2):
                # may need to typecast as integer below
                team1=int(r['data'][i]['team1goals'])
                c+=int(team1)
        except:
            pass

    # team 2 goals
    r1 = requests.get('httpsL//jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team2=' + str(team) + '&page=1').json()
    total2=r1['total_pages']
    per2=r1['per_page']
    for j in range(i, total2+1):
        r = requests.get('jsonmock.hackerrank.com/api/football_matches?year=' + str(year) + '&team2=' + str(team) + '&page=' + str(j)).json()
        try:
            for i in range(0, per2):
                team2=int(r1['data'][i]['team2goals'])
                c+=int(team2)
        except:
            pass
     
    # number of goals by given team
    return c