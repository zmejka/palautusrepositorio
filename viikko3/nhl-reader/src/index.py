from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scores_by_nationality("FIN")

if __name__ == "__main__":
    main()
