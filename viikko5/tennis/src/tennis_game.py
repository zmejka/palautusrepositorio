class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score1 = 0
        self.score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def score_str(self):
        names = {0:'Love', 1:'Fifteen', 2:'Thirty', 3:'Forty'}
        if self.score1 == self.score2:
            if self.score1 > 3:
                return 'Deuce'
            else:
                return f"{names[self.score1]}-All"
        return f"{names[self.score1]}-{names[self.score2]}"

    def results(self):
        difference = self.score1 - self.score2
        pretext = ""
        if abs(difference) == 1:
            pretext = 'Advantage'
        else:
            pretext = 'Win for'
        if difference > 0:
            return f"{pretext} {self.player1}"
        else:
            return f"{pretext} {self.player2}"

    def get_score(self):
        if self.score1 == self.score2:
            score = self.score_str()
        elif self.score1 >= 4 or self.score2 >= 4:
            score = self.results()
        else:
            score = self.score_str()
        return score
