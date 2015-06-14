from matches.models import Match
from teams.models import Team
from django.db.models import Q

def get_streaks(player):
    matches = player.matches

    print matches
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

    streaks = {
        'win_streak': win_streak,
        'best_win_streak': best_win_streak,
        'best_win_streak_date': best_win_streak_date,
        'not_lost_since': matches.exclude(winner=player.teams)[0].created,
        'losing_streak': losing_streak,
        'worst_losing_streak': worst_losing_streak,
        'worst_losing_streak_date': worst_losing_streak_date,
        'not_won_since': matches.filter(winner=player.teams)[0].created,
    }
    return streaks

