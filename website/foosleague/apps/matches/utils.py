import requests
from trueskill import rate, Rating, quality_1vs1
from players.models import Player
from math import sqrt
from trueskill.backends import cdf
from players.models import StatHistory
from trueskill import TrueSkill
from leagues.models import LeagueMember

from datetime import datetime


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
        winner_ratings.append(Rating(w.current_mu, w.current_sigma))

    for l in losers:
        loser_ratings.append(Rating(l.current_mu, l.current_sigma))

    winner_ratings, loser_ratings = rate([winner_ratings, loser_ratings])
    print winner_ratings
    print loser_ratings
    for counter, p in enumerate(winners):
        # p.ts_mu = winner_ratings[counter].mu
        # p.ts_sigma = winner_ratings[counter].sigma

        sh, _ = StatHistory.objects.get_or_create(player=p,
                                                  match=match,
                                                  )
        print match.season
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

    if team1_odds > team2_odds:
        normal_points = int(round(base_points * ((100 - team1_odds) / 100)))
        upset_points = int(round(base_points * ((100 - team2_odds) / 100)))
    else:
        normal_points = int(round(base_points * ((100 - team2_odds) / 100)))
        upset_points = int(round(base_points * ((100 - team1_odds) / 100)))

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
            # upset!
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

        # loser points

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
            # upset!
            for p in match.team_2.players.all():
                sh, _ = StatHistory.objects.get_or_create(player=p,
                                                          match=match)
                sh.season_points = upset_points
                sh.season = match.season

                sh.save()

        # loser points
        for p in match.team_1.players.all():
            sh, _ = StatHistory.objects.get_or_create(player=p, match=match)
            sh.season_points = -normal_points
            sh.season = match.season

            sh.save()


def regen_expose(match):
    env = TrueSkill(draw_probability=0)
    ratings = []
    players = Player.objects.filter(
        id__in=LeagueMember.objects.filter(league=match.league).values_list('player__id', flat=True))
    player_lookup = {}
    for p in players:
        rating = env.create_rating(p.current_mu, p.current_sigma)
        sh, _ = StatHistory.objects.get_or_create(player=p, match=match)
        sh.ts_expose = env.expose(rating)
        sh.save()
        p.ts_expose = env.expose(rating)
        p.save()
        ratings.append(rating)
        player_lookup.update({rating: p})

    leaderboard = sorted(ratings, key=env.expose, reverse=True)

def award_fooscoin(self):

    winners = self.winner.players.all()
    if self.winner == self.team_1:
        losers = self.team_2.players.all()
    else:
        losers = self.team_1.players.all()

    for player in winners:
        sh, _ = StatHistory.objects.get_or_create(player=player, match=self)
        sh.fooscoin = self.league.fooscoin_for_win
        sh.save()

    for player in losers:
        sh, _ = StatHistory.objects.get_or_create(player=player, match=self)
        sh.fooscoin = self.league.fooscoin_for_loss
        sh.save()


def recalculate_streaks(self):
    if self.winner == self.team_1:
        self.team_2.streak = 0
        self.team_1.streak += 1
        self.team_1.save()
        if self.team_1.streak > self.team_1.best_streak:
            self.team_1.best_streak = self.team_1.streak
            self.team_1.best_streak_date = datetime.now()

    else:
        self.team_1.streak = 0
        self.team_2.streak += 1

        if self.team_2.streak > self.team_2.best_streak:
            self.team_2.best_streak = self.team_2.streak
            self.team_2.best_streak_date = datetime.now()

    self.team_1.save()
    self.team_2.save()
    self.save()

def broadcast_message(self, winning_score, losing_score, loser, request):
    if self.team_2_score == 0 or self.team_1_score == 0:
        message = ":skunk: :skunk: :skunk: *%s* _(%s)_ vs *%s* _(%s)_ :skunk: :skunk: :skunk: (http://%s.foosleague.com%s)" % (self.winner,
                                                                                                                               winning_score, loser, losing_score, request.league.subdomain, self.get_absolute_url())
    else:
        message = "Game Over! *%s* _(%s)_ vs *%s* _(%s)_ (http://%s.foosleague.com%s)" % (self.winner,
                                                                                          winning_score, loser,  losing_score, request.league.subdomain, self.get_absolute_url())

    requests.post('https://liftinteractive.slack.com/services/hooks/slackbot?token=%s&channel=%s' % (request.league.slack_token, "%23" + request.league.slack_channel,),
                  data=message)