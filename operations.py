import json
import datetime as dt
import urllib.request

date_format = '%Y-%m-%d'
result = []


def api_url(url_type, start_date=None, end_date=None):
    if url_type == "team":
        url = "https://delivery.chalk247.com/team_rankings/NFL.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0"
    elif url_type == "score":
        url = f"https://delivery.chalk247.com/scoreboard/NFL/{start_date}/{end_date}.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0"
    return url


def accept_input(string):
    while True:
        try:
            date = input("Enter {} (YYYY-MM-DD): ".format(string))
            formatted_date = dt.datetime.strptime(date, date_format)
        except ValueError:
            print('Enter the valid date in format YYYY-MM-DD')
            continue
        else:
            return date, formatted_date
            break

def team_rank(id):
    team_rankings = api_url("team")
    url_tr = urllib.request.urlopen(team_rankings)
    team_data= json.loads(url_tr.read().decode())
    for rank in team_data['results']['data']:
        if rank['team_id'] == id:
            return {"rank": rank['rank'],"points": rank['adjusted_points']}


def scoreboard(start_date, end_date):
    url = api_url("score", start_date, end_date)
    response = urllib.request.urlopen(url)
    scoreboard = json.loads(response.read().decode())
    for date in scoreboard['results']:
        try:
            for id in scoreboard['results'][date]['data']:
                event = {}
                event_data = scoreboard['results'][date]['data'][id]

                date_time_obj = dt.datetime.strptime(event_data['event_date'], '%Y-%m-%d %H:%M')
                away_rank_points = team_rank(event_data['away_team_id'])
                home_rank_points = team_rank(event_data['home_team_id'])

                event = {
                    "event_id": event_data['event_id'],
                    "event_date": date_time_obj.strftime('%d-%m-%Y'),
                    "event_time": date_time_obj.strftime('%H:%M'),
                    "away_team_id": event_data['away_team_id'],
                    "away_nick_name": event_data['away_nick_name'],
                    "away_city": event_data['away_city'],
                    "away_rank": away_rank_points['rank'],
                    "away_rank_points": away_rank_points['points'],
                    "home_team_id": event_data['home_team_id'],
                    "home_nick_name": event_data['home_nick_name'],
                    "home_city": event_data['home_city'],
                    "home_rank": home_rank_points['rank'],
                    "home_rank_points": home_rank_points['points']
                }
                result.append(event)
        except:
            continue
    return result
