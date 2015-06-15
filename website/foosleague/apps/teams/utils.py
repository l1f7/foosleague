from django.db.models import Q, Sum
from datetime import datetime, timedelta


def get_streaks(team):
    matches = team.matches.order_by('created')

    win_streak = 0
    best_win_streak = 0
    losing_streak= 0
    worst_losing_streak = 0
    best_win_streak_date = ""
    worst_losing_streak_date = ""
    first_loss = None
    first_win = None
    loss_spanning_days = None
    win_spanning_days = None

    for m in matches:
        if m.winner == team:
            # He/She Won

            if losing_streak == worst_losing_streak:
                last_loss = m
                try:
                    loss_spanning_days = (last_loss.created-first_loss.created).days+1

                except:
                    loss_spanning_days = None

            win_streak += 1
            losing_streak = 0

            if win_streak == 1:
                #first win, mark it!
                first_win = m

            if win_streak > best_win_streak:
                best_win_streak = win_streak
                best_win_streak_date = m.created


        else:
            # He/She Lost
            if win_streak == best_win_streak and win_streak > 1:
                last_win = m
                win_spanning_days = (last_win.created - first_win.created).days +1

            win_streak = 0
            losing_streak += 1
            if losing_streak == 1:
                #first loss, mark it!
                first_loss = m

            if losing_streak > worst_losing_streak:

                worst_losing_streak = losing_streak
                if losing_streak == 1:
                    # first loss, mark the date
                    first_loss = m
                    worst_losing_streak_date = m.created

        last_game = m

    not_lost_since = None
    not_won_since = None

    if win_streak > 0:
        try:
            not_lost_since = matches.exclude(winner=team)[0].created
        except:
            not_lost_since = "Never"

        if win_streak == best_win_streak:
            win_spanning_days = (last_game.created - first_win.created).days +1

    if losing_streak > 0:
        try:
            not_won_since = matches.filter(winner=team)[0].created
        except:
            not_won_since = "Well, never"
        if losing_streak == worst_losing_streak:
            loss_spanning_days = (last_game.created - first_loss.created).days +1

    streaks = {
        'win_streak': win_streak,
        'best_win_streak': best_win_streak,
        'best_win_streak_date': best_win_streak_date,
        'win_spanning_days': win_spanning_days,
        'not_lost_since': not_lost_since,
        'losing_streak': losing_streak,
        'loss_spanning_days': loss_spanning_days,
        'worst_losing_streak': worst_losing_streak,
        'worst_losing_streak_date': worst_losing_streak_date,
        'not_won_since': not_won_since,
    }
    return streaks