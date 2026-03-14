import duckdb

db_path = "data/db/sdss.duckdb"
csv_path = "data/csv/raw_data.csv"

conn = duckdb.connect(db_path)

conn.execute(f"""
CREATE TABLE raw_sdss AS
SELECT *
FROM read_csv_auto('{csv_path}');
""")

conn.execute("""
CREATE TABLE processed_sdss AS
SELECT
    row_number() OVER () AS id,
    *
FROM raw_sdss
""")

conn.execute("""
CREATE VIEW processed_sdss_view AS
SELECT
    id,
    (u - g) AS u_g,
    (g - r) AS g_r,
    (r - i) AS r_i,
    (i - z) AS i_z,
    (u - r) AS u_r,
    (g - i) AS g_i,
    (g - z) AS g_z,
    (psfMag_r - modelMag_r) AS morphology_r,
    (psfMag_g - modelMag_g) AS morphology_g,
    class AS target_class
FROM processed_sdss
""")

conn.close()
