from trueskill import rate, Rating, quality_1vs1
from players.models import Player
from matches.models import Match


def update_trueskill(match):
    winner = match.winner
    print winner
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
        p.ts_mu = winner_ratings[counter].mu
        p.ts_sigma = winner_ratings[counter].sigma
        p.save()

    for counter, p in enumerate(losers):
        p.ts_mu = loser_ratings[counter].mu
        p.ts_sigma = loser_ratings[counter].sigma
        p.save()



# from math import sqrt
# from trueskill.backends import cdf

# def Pwin(rAlist=[Rating()],  rBlist=[Rating()]):
#     deltaMu = sum( [x.mu for x in rAlist])  - sum( [x.mu for x in  rBlist])
#     rsss = sqrt(sum( [x.sigma**2 for x in  rAlist]) + sum( [x.sigma**2 for x in rBlist]) )
#     return cdf(deltaMu/rsss)



# matches = Match.objects.all()
# right = 0
# wrong = 0
# for m in matches:
#     team1 = []
#     team2 = []
#     for p in m.team_1.players.all():
#         team1.append(Rating(p.ts_mu, p.ts_sigma))
#     for p in m.team_2.players.all():
#         team2.append(Rating(p.ts_mu, p.ts_sigma))
#     team1_wp = round((Pwin(team1, team2)*100),2)
#     team2_wp = round((Pwin(team2, team1)*100), 2)
#     print '%s (%s percent) - %s (%s precent) winner: %s' % (m.team_1, team1_wp, m.team_2, team2_wp, m.winner)
#     if m.team_1 == m.winner:
#         if team1_wp > team2_wp:
#             right += 1
#         else:
#             wrong += 1
#     else:
#         if team2_wp > team1_wp:
#             right += 1
#         else:
#             wrong += 1

# print 'Right: %s Wrong: %s' % (right, wrong,)



def recalc_trueskill():

    players = Player.objects.all()
    for p in players:
        p.ts_mu = 25
        p.ts_mu = 8.33333
        p.save()

    matches = Match.objects.all().order_by('created')

    for m in matches:
        update_trueskill(m)
