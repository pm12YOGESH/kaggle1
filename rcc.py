import pandas as pd

pd.options.display.min_rows = 100
pd.options.display.max_rows = 100

leaderboard = pd.read_csv('/kaggle/input/notebooks/ryanholbrook/rsna-knee-abnormalities-efficiency-data/leaderboard.csv', index_col='EfficiencyRank')
leaderboard.to_csv('full_leaderboard.csv')
leaderboard.head(100)
