from trueskill import rate, Rating, quality_1vs1
from players.models import Player
from math import sqrt
from trueskill.backends import cdf
from players.models import StatHistory


def update_trueskill(match):
    winner = match.winner

    if match.team_1 == winner:
        loser = match.team_2
    else:
        loser = match.team_1

    winners = winner.players.all()
    losers = loser.players.all()

    winner_ratings = []
    loser_ratings = []

    for w in winners:
        winner_ratings.append(Rating(w.ts_mu, w.ts_sigma))

    for l in losers:
        loser_ratings.append(Rating(l.ts_mu, l.ts_sigma))

    winner_ratings, loser_ratings = rate([winner_ratings, loser_ratings])

    for counter, p in enumerate(winners):
        # p.ts_mu = winner_ratings[counter].mu
        # p.ts_sigma = winner_ratings[counter].sigma

        sh, _ = StatHistory.objects.get_or_create(player=p,
                                                  match=match,
                                                  )
        sh.season = match.season
        sh.ts_mu = winner_ratings[counter].mu
        sh.ts_sigma = winner_ratings[counter].sigma
        sh.save()
        # p.save()

    for counter, p in enumerate(losers):
        # p.ts_mu = loser_ratings[counter].mu
        # p.ts_sigma = loser_ratings[counter].sigma
        sh, _ = StatHistory.objects.get_or_create(player=p,
                                                  match=match,
                                                  )
        sh.season = match.season
        sh.ts_mu = loser_ratings[counter].mu
        sh.ts_sigma = loser_ratings[counter].sigma
        sh.save()

def Pwin(rAlist=[Rating()],  rBlist=[Rating()]):
    deltaMu = sum([x.mu for x in rAlist]) - sum([x.mu for x in rBlist])
    rsss = sqrt(sum([x.sigma**2 for x in rAlist]) + sum([x.sigma**2 for x in rBlist]))
    return cdf(deltaMu / rsss)


def winning_percentage(match, team):

    team1 = []
    team2 = []
    for p in match.team_1.players.all():
        team1.append(Rating(p.ts_mu, p.ts_sigma))
    for p in match.team_2.players.all():
        team2.append(Rating(p.ts_mu, p.ts_sigma))

    if team == 1:
        return round((Pwin(team1, team2) * 100), 2)
    else:
        return round((Pwin(team2, team1) * 100), 2)


def calculate_odds():

    matches = Match.objects.all()
    right = 0
    wrong = 0
    for m in matches:
        team1 = []
        team2 = []
        for p in m.team_1.players.all():
            team1.append(Rating(p.ts_mu, p.ts_sigma))
        for p in m.team_2.players.all():
            team2.append(Rating(p.ts_mu, p.ts_sigma))
        team1_wp = round((Pwin(team1, team2) * 100), 2)
        team2_wp = round((Pwin(team2, team1) * 100), 2)
        print '%s (%s percent) - %s (%s precent) winner: %s' % (m.team_1, team1_wp, m.team_2, team2_wp, m.winner)
        if m.team_1 == m.winner:
            if team1_wp > team2_wp:
                right += 1
            else:
                wrong += 1
        else:
            if team2_wp > team1_wp:
                right += 1
            else:
                wrong += 1

    print 'Right: %s Wrong: %s' % (right, wrong,)


def recalc_trueskill():
    from matches.models import Match

    # reset players
    players = Player.objects.all()
    for p in players:
        p.ts_mu = 25
        p.ts_sigma = 8.33333
        p.save()

    matches = Match.objects.all().order_by('created')

    for m in matches:
        update_trueskill(m)


def award_season_points(match):
    team1_odds = winning_percentage(match, 1)
    team2_odds = winning_percentage(match, 2)
    base_points = match.league.base_match_points

    base_points = match.league.base_match_points

    if team1_odds > team2_odds:
        normal_points = int(round(base_points * ((100 - team1_odds) / 100)))
        upset_points = int(round(base_points * ((100-team2_odds) / 100)))
    else:
        normal_points = int(round(base_points * ((100 - team2_odds) / 100)))
        upset_points = int(round(base_points * ((100-team1_odds) / 100)))

    if match.winner == match.team_1:
        # winner points
        if team1_odds > team2_odds:
            for p in match.team_1.players.all():
                sh, _ = StatHistory.objects.get_or_create(player=p,
                                           match=match)
                sh.season_points = normal_points
                sh.season = match.season
                sh.save()



        else:
            #upset!
            for p in match.team_1.players.all():
                sh, _ = StatHistory.objects.get_or_create(player=p,
                                           match=match)
                sh.season_points = upset_points
                sh.season = match.season

                sh.save()


        for p in match.team_2.players.all():
            sh, _ = StatHistory.objects.get_or_create(player=p, match=match)
            sh.season_points = -normal_points
            sh.season = match.season

            sh.save()

        #loser points

    else:
        # winner points
        if team2_odds > team1_odds:
            for p in match.team_2.players.all():
                sh, _ = StatHistory.objects.get_or_create(player=p,
                                           match=match)
                sh.season_points = normal_points
                sh.season = match.season

                sh.save()
        else:
            #upset!
            for p in match.team_2.players.all():
                sh, _ = StatHistory.objects.get_or_create(player=p,
                                           match=match)
                sh.season_points = upset_points
                sh.season = match.season

                sh.save()

        #loser points
        for p in match.team_1.players.all():
            sh, _ = StatHistory.objects.get_or_create(player=p, match=match)
            sh.season_points = -normal_points
            sh.season = match.season

            sh.save()