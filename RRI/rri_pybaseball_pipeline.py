# RRI Data Pipeline using pybaseball
from pybaseball import pitching_stats, playerid_lookup
import pandas as pd
from datetime import datetime

# Set year dynamically or manually
current_year = datetime.now().year

# Pull raw pitching stats (seasonal)
print(f"Fetching pitching stats for {current_year}...")
df = pitching_stats(start_season=current_year, end_season=current_year, qual=0)

# Filter to relievers: less than 90 IP, more than 10 appearances
relievers = df[(df['IP'] < 90) & (df['G'] > 10)].copy()

# Add RRI-specific columns for scoring model
relievers['K_BB%'] = relievers['K%'] - relievers['BB%']
relievers['K_BB'] = relievers['SO'] / relievers['BB']  # Raw ratio for RRI K/BB factor

# Optional: Add team tier, prospect status, or injury flags via join with your lookup
# merged = relievers.merge(player_lookup_table, on='player_id', how='left')

# Save locally or upload to Google Sheets/Databricks
relievers.to_csv(f'rri_relievers_{current_year}.csv', index=False)
print(f"✅ Exported {len(relievers)} relievers to CSV.")
