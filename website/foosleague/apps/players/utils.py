from django.db.models import Q, Sum
from datetime import datetime, timedelta


def get_streaks(player):
    matches = player.matches.order_by('created')

    win_streak = 0
    best_win_streak = 0
    losing_streak= 0
    worst_losing_streak = 0
    best_win_streak_date = ""
    worst_losing_streak_date = ""

    for m in matches:
        if m.winner in player.teams:
            win_streak += 1
            losing_streak = 0
            if win_streak > best_win_streak:
                best_win_streak = win_streak
                best_win_streak_date = m.created
        else:
            win_streak = 0
            losing_streak += 1
            if losing_streak > worst_losing_streak:
                worst_losing_streak = losing_streak
                if losing_streak == 1:
                    # first loss, mark the date
                    worst_losing_streak_date = m.created

    not_lost_since = None
    not_won_since = None

    if win_streak:
        not_lost_since = matches.exclude(winner=player.teams)[0].created
    if losing_streak:
        not_won_since = matches.filter(winner=player.teams)[0].created

    streaks = {
        'win_streak': win_streak,
        'best_win_streak': best_win_streak,
        'best_win_streak_date': best_win_streak_date,
        'not_lost_since': not_lost_since,
        'losing_streak': losing_streak,
        'worst_losing_streak': worst_losing_streak,
        'worst_losing_streak_date': worst_losing_streak_date,
        'not_won_since': not_won_since,
    }
    return streaks


def calc_wins(player, days=None, season=False):
    today = datetime.today()
    wins = player.matches.filter(winner__in=player.teams)
    if days:
        wins = wins.filter(created__gte=today-timedelta(days=days), created__lte=today)

    if season:
        try:
            season = Season.objects.get(start__lte=today, end__gte=today)
            wins.filter(season=season)
        except:
            return '--'

    return wins.count()


def calc_loses(player, days=None, season=False):
    today = datetime.today()
    loses = player.maytches.exclude(winner__in=player.teams)
    if days:
        loses = loses.filter(created__gte=today-timedelta(days=days), created_lte=today)
    if season:
        try:
            season = Season.objects.get(start__lte=today, end__gte=today)
            wins.filter(season=season)
        except:
            return '--'
    return loses.count()


def calc_goal_differential(player, days=None, direction='for', season=None):
    goals_for = 0
    goals_against = 0
    today = datetime.today()
    teams = player.teams
    if days:
        team1_goals = player.matches.filter(created__gte=today - timedelta(days=7), created__lte=today,
                                     team_1__in=teams).aggregate(goals_as_team1=Sum('team_1_score'), goals_against=Sum('team_2_score'))
        goals_for = team1_goals['goals_as_team1'] or 0
        goals_against = team1_goals['goals_against'] or 0

        team2_goals = player.matches.filter(created__gte=today - timedelta(days=7), created__lte=today,
                                     team_2__in=teams).aggregate(goals_as_team2=Sum('team_2_score'), goals_against=Sum('team_1_score'))
        goals_for += team2_goals['goals_as_team1'] or 0
        goals_against += team2_goals['goals_against'] or 0

    elif season:
        try:
            current_season = Season.objects.get(start__lte=today, end__gte=today)

            team1_goals = player.matches.filter(team_1__in=teams, season=current_season).aggregate(
                goals_as_team1=Sum('team_1_score'), goals_against=Sum('team_2_score'))
            goals_for = team1_goals['goals_as_team1'] or 0
            goals_against = team1_goals['goals_against'] or 0

            # team 2 goals
            team2_goals = player.matches.filter(team_2__in=teams, season=current_season).aggregate(
                goals_as_team2=Sum('team_2_score'), goals_against=Sum('team_1_score'))
            goals_for+= team2_goals['goals_as_team2'] or 0
            goals_against += team2_goals['goals_against'] or 0
        except:
            goals_for = ''
            goals_against = ''

    if direction == 'for':
        return goals_for
    else:
        return goals_against

    return {'for': goals_for, 'against': goals_against}


def calc_color_preference(player, color='red', stat='favoured'):

        #which team you've won the most with
        red_plays = float(matches.filter(team_1=teams).count())
        red_wins = float(matches.filter(winner=teams, team_1=teams).count())
        black_plays = float(matches.filter(team_2=teams).count())
        black_wins = float(matches.filter(winner=teams, team_2=teams).count())

        color_stats = {}
        if color == 'red':
            if stat == 'favoured':
                return int(round((red_wins/red_plays*100)))
            else:
                return int(round((red_plays/(red_plays+black_plays))*100))
        else:
            if stat == 'favoured':
                return int(round((black_wins/black_plays*100)))
            else:
                return int(round((black_plays/(red_plays+black_plays))*100))

def calc_stats(player):
    today = datetime.today()
    teams = player.teams
    matches = player.matches
    from seasons.models import Season
    current_season = Season.objects.filter(start__lte=today, end__gte=today)


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
            'favoured': int(round((red_wins/red_plays)*100)),
            'winning_percentage': int(round((red_plays/(red_plays+black_plays))*100))
        }
    if black_plays:
        color_stats['black'] = {
            'favoured': int(round((black_wins/black_plays)*100)),
            'winning_percentage': int(round((black_plays/(red_plays+black_plays))*100))
        }

    stats = {
        'wins': wins,
        'losses': losses,
        'goal_differential': goal_differential,
        'color_stats': color_stats,
    }
    return stats
