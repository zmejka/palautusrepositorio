import requests
from player import Player
from datetime import datetime

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)

    print("Players from FIN", datetime.now())
    print()

    fin_players = []
    for player in players:
        if player.nationality == 'FIN':
            fin_players.append(player)
    fin_players.sort(key=lambda x:x.score, reverse=True)
    
    for player in fin_players:
        print(player)

if __name__ == "__main__":
    main()
