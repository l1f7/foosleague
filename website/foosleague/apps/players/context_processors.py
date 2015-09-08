from .models import Player
from datetime import datetime, timedelta
from django.db.models import Q, Sum

from teams.models import Team
from matches.models import Match
from seasons.models import Season


def player(request):
    # try:
    today = datetime.today()
    if request.user.is_authenticated():
        player = Player.objects.get(user=request.user)
        teams = Team.objects.filter(players=player)
        current_season = Season.objects.filter(league=request.league, start__lte=today, end__gte=today)

        matches = Match.objects.filter(Q(team_1__in=teams) | Q(team_2__in=teams), league=request.league, season=current_season)
        wins = {
            '7': matches.filter(winner__in=teams, created__gte=today - timedelta(days=7), created__lte=today).count(),
            '30': matches.filter(winner__in=teams, created__gte=today - timedelta(days=30), created__lte=today).count(),
            'season': matches.filter(winner__in=teams, season=current_season).count()
        }

        losses = {
            '7': matches.filter(created__gte=today - timedelta(days=7), created__lte=today).exclude(winner__in=teams).count(),

            '30': matches.filter(created__gte=today - timedelta(days=30), created__lte=today).exclude(winner__in=teams).count(),
            'season': matches.filter(season=current_season).exclude(winner__in=teams).count()
        }

        # 7 day goal differential
        goals_for = {}
        goals_against = {}
        # team 1 goals
        team1_goals = matches.filter(created__gte=today - timedelta(days=7), created__lte=today,
                                     team_1__in=teams).aggregate(goals_as_team1=Sum('team_1_score'), goals_against=Sum('team_2_score'))
        goals_for[7] = team1_goals['goals_as_team1'] or 0
        goals_against[7] = team1_goals['goals_against'] or 0

        # team 2 goals
        team2_goals = matches.filter(created__gte=today - timedelta(days=7), created__lte=today,
                                     team_2__in=teams).aggregate(goals_as_team2=Sum('team_2_score'), goals_against=Sum('team_1_score'))
        goals_for[7] += team2_goals['goals_as_team2'] or 0
        goals_against[7] += team2_goals['goals_against'] or 0

        # 30 day goal differential
        team1_goals = matches.filter(created__gte=today - timedelta(days=7), created__lte=today,
                                     team_1__in=teams).aggregate(goals_as_team1=Sum('team_1_score'), goals_against=Sum('team_2_score'))
        goals_for[30] = team1_goals['goals_as_team1'] or 0
        goals_against[30] = team1_goals['goals_against'] or 0

        # team 2 goals
        team2_goals = matches.filter(created__gte=today - timedelta(days=30), created__lte=today,
                                     team_2__in=teams).aggregate(goals_as_team2=Sum('team_2_score'), goals_against=Sum('team_1_score'))
        goals_for[30] += team2_goals['goals_as_team2'] or 0
        goals_against[30] += team2_goals['goals_against'] or 0

        # Season goal differential
        team1_goals = matches.filter(team_1__in=teams, season=current_season).aggregate(
            goals_as_team1=Sum('team_1_score'), goals_against=Sum('team_2_score'))
        goals_for['season'] = team1_goals['goals_as_team1'] or 0
        goals_against['season'] = team1_goals['goals_against'] or 0

        # team 2 goals
        team2_goals = matches.filter(team_2__in=teams, season=current_season).aggregate(
            goals_as_team2=Sum('team_2_score'), goals_against=Sum('team_1_score'))
        goals_for['season'] += team2_goals['goals_as_team2'] or 0
        goals_against['season'] += team2_goals['goals_against'] or 0

        goal_differential = {
            '7': {
                'for': goals_for[7],
                'against': goals_against[7]
            },
            '30': {
                'for': goals_for[30],
                'against': goals_against[30]
            },
            'season': {
                'for': goals_for['season'],
                'against': goals_against['season']
            }
        }

        #which team you've won the most with
        red_plays = float(matches.filter(team_1=teams).count())
        red_wins = float(matches.filter(winner=teams, team_1=teams).count())
        black_plays = float(matches.filter(team_2=teams).count())
        black_wins = float(matches.filter(winner=teams, team_2=teams).count())

        color_stats = {}
        if red_plays:
            color_stats['red'] = {
                'winning_percentage': int(round((red_wins/red_plays)*100)),
                'favoured': int(round((red_plays/(red_plays+black_plays))*100))
            }
        if black_plays:
            color_stats['black'] = {
                'winning_percentage': int(round((black_wins/black_plays)*100)),
                'favoured': int(round((black_plays/(red_plays+black_plays))*100))
            }

        stats = {
            'wins': wins,
            'losses': losses,
            'goal_differential': goal_differential,
            'color_stats': color_stats,
        }

        return {'player': player, 'stats': stats}
    else:
        return {}
