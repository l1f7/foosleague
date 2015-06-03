from trueskill import rate, Rating


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

