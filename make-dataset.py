
import os
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


match_awayteam_df = pd.DataFrame()
match_awayteamscore_df = pd.DataFrame()
match_event_df = pd.DataFrame()
match_hometeam_df = pd.DataFrame()
match_hometeamscore_df = pd.DataFrame()
match_round_df = pd.DataFrame()
match_season_df = pd.DataFrame()
match_time_df = pd.DataFrame()
match_tournament_df = pd.DataFrame()
match_venue_df = pd.DataFrame()

for file in os.listdir("tennis_data/raw/raw_match_parquet"):
    if file.startswith("away_team_1"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        if not singel_stats.empty and not singel_stats.isna().all().all():
            match_awayteam_df = pd.concat([match_awayteam_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("away_team_score"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_awayteamscore_df = pd.concat([match_awayteamscore_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("event"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_event_df = pd.concat([match_event_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("home_team_1"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        if not singel_stats.empty and not singel_stats.isna().all().all():
            match_hometeam_df = pd.concat([match_hometeam_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("home_team_score"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_hometeamscore_df = pd.concat([match_hometeamscore_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("round"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_round_df = pd.concat([match_round_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("season"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_season_df = pd.concat([match_season_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("time"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_time_df = pd.concat([match_time_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("tournament"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_tournament_df = pd.concat([match_tournament_df, singel_stats], axis="rows", ignore_index=True)
    elif file.startswith("venue"):    
        singel_stats = pd.read_parquet("tennis_data/raw/raw_match_parquet/" + file)
        match_venue_df = pd.concat([match_venue_df, singel_stats], axis="rows", ignore_index=True)
    

odds_df = pd.DataFrame()

for file in os.listdir("tennis_data/raw/raw_odds_parquet"):    
    singel_stats = pd.read_parquet("tennis_data/raw/raw_odds_parquet/" + file)
    odds_df = pd.concat([odds_df, singel_stats], axis="rows", ignore_index=True)


pbp_df = pd.DataFrame()

for file in os.listdir("tennis_data/raw/raw_point_by_point_parquet"):    
    singel_stats = pd.read_parquet("tennis_data/raw/raw_point_by_point_parquet/" + file)
    pbp_df = pd.concat([pbp_df, singel_stats], axis="rows", ignore_index=True)


statistics_df = pd.DataFrame()

for file in os.listdir("tennis_data/raw/raw_statistics_parquet"):    
    singel_stats = pd.read_parquet("tennis_data/raw/raw_statistics_parquet/" + file)
    statistics_df = pd.concat([statistics_df, singel_stats], axis="rows", ignore_index=True)


power_df = pd.DataFrame()

for file in os.listdir("tennis_data/raw/raw_tennis_power_parquet"):    
    singel_stats = pd.read_parquet("tennis_data/raw/raw_tennis_power_parquet/" + file)
    power_df = pd.concat([power_df, singel_stats], axis="rows", ignore_index=True)


votes_df = pd.DataFrame()

for file in os.listdir("tennis_data/raw/raw_votes_parquet"):    
    singel_stats = pd.read_parquet("tennis_data/raw/raw_votes_parquet/" + file)
    votes_df = pd.concat([votes_df, singel_stats], axis="rows", ignore_index=True)


global_vars = dict(globals())

for var_name, var_value in global_vars.items():
    # Check if the variable is a DataFrame
    if isinstance(var_value, pd.DataFrame):
        # Save as CSV using the variable name
        var_value.to_csv(f"tennis_data/csv-file/{var_name}.csv", index=False)
        print(f"Saved {var_name}.csv")