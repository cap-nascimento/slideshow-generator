import psycopg2
import pandas as pd

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="bdodump",
    user="postgres",
    password="pgsql",
    host="localhost",
    port="5432"
)

# Define your SQL query
sql_query = "SELECT * FROM auth_user;"

# Execute the query and fetch the results
df = pd.read_sql_query(sql_query, conn)

# Close the database connection
conn.close()

# Display the DataFrame
print(df)
