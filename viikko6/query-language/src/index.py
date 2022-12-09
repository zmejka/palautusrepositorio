from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from querybuilder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = (query.
                playsIn("NYR").
                hasAtLeast(10, "goals").
                hasFewerThan(20, "goals").
                build()
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
