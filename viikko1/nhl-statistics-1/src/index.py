from statistics import Statistics
from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def main():
    reader = PlayerReader()
    stats = Statistics(reader)
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10, SortBy.POINTS)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
