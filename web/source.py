import datetime

import requests


class Bundesliga:

    def bundesliga_season(self):
        address = 'https://www.openligadb.de/api/getmatchdata/bl1/2021'
        info = requests.get(address)
        return info.json()

    def bundesliga_teams(self):
        address = 'https://www.openligadb.de/api/getavailableteams/bl1/2021'
        info = requests.get(address)
        return info.json()

    def bundesliga_weekend(self):
        current_season = self.bundesliga_season()
        today = datetime.date.today()
        sat = today + datetime.timedelta((5 - today.weekday()) % 7)
        sun = today + datetime.timedelta((6 - today.weekday()) % 7)

        weekdays = {'Saturday': sat, 'Sunday': sun}
        result = []

        for match in current_season:
            date = match["MatchDateTime"]
            transformed_day = str(date[0:10])
            if transformed_day == str(weekdays['Saturday']) or transformed_day == str(weekdays['Sunday']):
                result.append(match)

        return result

    def bundesliga_table(self):
        bundesliga_teams = self.bundesliga_teams()
        season = self.bundesliga_season()

        ranking = {}
        for team in bundesliga_teams:
            ranking[team['TeamId']] = {
                'team_name': team['TeamName'],
                'points': 0,
                'wins': 0,
                'loses': 0,
                'draws': 0,
                'goals': 0,
                'received_goals': 0,
            }

        for m in season:
            if not m["MatchIsFinished"]:
                continue

            team_one = m["Team1"]["TeamId"]
            team_two = m["Team2"]["TeamId"]

            if m["MatchResults"]:
                goals_one = int(m["MatchResults"][0]["PointsTeam1"])
                goals_two = int(m["MatchResults"][0]["PointsTeam2"])

                if goals_one > goals_two:
                    ranking[team_one]['wins'] += 1
                    ranking[team_one]['points'] += 3
                    ranking[team_two]['loses'] += 1
                elif goals_one < goals_two:
                    ranking[team_two]['wins'] += 1
                    ranking[team_two]['points'] += 3
                    ranking[team_one]['loses'] += 1
                else:
                    ranking[team_one]['points'] += 1
                    ranking[team_two]['points'] += 1
                    ranking[team_two]['draws'] += 1
                    ranking[team_one]['draws'] += 1
        return sorted([v for k, v in ranking.items()], key=lambda x: x["points"], reverse=True)

    def bundesliga_all_upcoming(self):
        current_season = self.bundesliga_season()
        today = datetime.datetime.now()
        result = []

        for match in current_season:
            date = match["MatchDateTime"]
            transformed_day = str(date[0:10])
            expected_date = datetime.datetime.strptime(transformed_day, "%Y-%m-%d")
            if expected_date > today:
                result.append(match)

        return result

