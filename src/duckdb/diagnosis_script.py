import duckdb

conn = duckdb.connect("data/db/sdss.duckdb")

print("Tables:")
print(conn.execute("SHOW TABLES").fetchall())

print("\nPreview data:")
print(conn.execute("SELECT * FROM raw_sdss LIMIT 5").fetch_df())

conn.close()