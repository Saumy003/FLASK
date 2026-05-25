import pandas as pd
import numpy as np

ipl_matches = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv"

matches = pd.read_csv(ipl_matches)

matches.head()

# print(list(set(list(matches["Team1"]) + list(matches["Team2"]))))

team1 = "Rajasthan Royals"
team2 = "Royal Challengers Bangalore"

temp_df = matches[((matches["Team1"] == team1) & (matches["Team2"] == team2)) | ((matches["Team1"] == team2) & (matches["Team2"] == team1))]

total_matches = temp_df.shape[0]

# print(total_matches)
# temp_df["WinningTeam"].value_counts()


matches_won_team1 = temp_df["WinningTeam"].value_counts().get(team1, 0)
matches_won_team2 = temp_df["WinningTeam"].value_counts().get(team2, 0)

draws = total_matches - (matches_won_team1 + matches_won_team2)

def team_vs_team(team1, team2):
    temp_df = matches[(matches["Team1"] == team1) & (matches["Team2"] == team2) | (matches["Team1"] == team2) & (matches["Team2"] == team1)]

    total_matches = temp_df.shape[0]
    draws = total_matches - (matches_won_team1 + matches_won_team2)

    response = {
        "total_matches" : str(total_matches),
        team1 : str(matches_won_team1),
        team2 : str(matches_won_team2),
        "draws" : str(draws)
    }

    return response

won =  team_vs_team("Rajasthan Royals" , "Royal Challengers Bangalore")
print(won)

