import pandas as pd
from fetch import DbConnection
from sql_queries import *


def fetch_rankings(dbconn):
  return {
    "general": dbconn.execute_query(general_ranking_sql),
    "technical": dbconn.execute_query(tec_ranking_sql),
    "maincat": dbconn.execute_query(main_ranking_sql),
    "lucky": dbconn.execute_query(lucky_ranking_sql)
  }
  

def fetch_random_bets(dbconn):
  return dbconn.execute_query(random_bets_sql)


def fetch_ai_descriptions(dbconn):
  return dbconn.execute_query(ai_descriptions_sql)


def filtered_ranking(df, df_name, field, is_max):
  if is_max:
    return df[df_name][df[df_name][field] == df[df_name][field].max()]
  return df[df_name][df[df_name][field] == df[df_name][field].min()]


def results():
  dbconn = DbConnection()
  
  rankings = fetch_rankings(dbconn)
  random_bets = fetch_random_bets(dbconn)
  ai_descriptions = fetch_ai_descriptions(dbconn)
  
  for key, value in rankings.items():
    rankings[key] = rankings[key][rankings[key]['username'] != 'moltres-admin']
  
  random_bets = random_bets[random_bets['username'] != 'moltres-admin']
  dbconn.close_conn()
  
  return {
    # "general": filtered_ranking(rankings, "general", "right_choices", True),
    # "technical": filtered_ranking(rankings, "technical", "right_choices", True),
    # "maincat": filtered_ranking(rankings, "maincat", "right_choices", True),
    # "lucky": filtered_ranking(rankings, "lucky", "right_choices", True),
    # "razzle": filtered_ranking(rankings, "general", "right_choices", False),
    "general": rankings["general"].sort_values(by="right_choices", ascending=False),
    "technical": rankings["technical"].sort_values(by="right_choices", ascending=False),
    "maincat": rankings["maincat"].sort_values(by="right_choices", ascending=False),
    "lucky": rankings["lucky"].sort_values(by="right_choices", ascending=False),
    "razzle": filtered_ranking(rankings, "general", "right_choices", False),
    "all": rankings["general"].sort_values(by="right_choices", ascending=False),
    "randoms": random_bets,
    "ai_descriptions": ai_descriptions,
  }