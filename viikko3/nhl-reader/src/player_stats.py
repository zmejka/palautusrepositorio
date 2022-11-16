from datetime import datetime
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, reader:PlayerReader):
        self.players = []
        self.lista = reader.get_players()

    def top_scores_by_nationality(self, nationality):

        print(f"Players from {nationality}", datetime.now())
        print()

        for player in self.lista:
            if player.nationality == nationality:
                self.players.append(player)
        self.players.sort(key=lambda x:x.score, reverse=True)

        for player in self.players:
            print(player)
