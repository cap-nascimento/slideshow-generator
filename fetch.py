import psycopg2
import pandas as pd
from config import *


class DbConnection():
  conn = psycopg2.connect(
    dbname=PG_DATABASE,
    user=PG_USER,
    password=PG_PASSWORD,
    host=PG_HOST,
    port=PG_PORT,
    client_encoding="UTF-8"
  )
  
  def execute_query(self, sql_query):
    df = pd.read_sql_query(sql_query, self.conn)
    return df
  
  def close_conn(self):
    self.conn.close()