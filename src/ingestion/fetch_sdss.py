from astroquery.sdss import SDSS

query = """
SELECT TOP 100
ra, dec, u, g, r, i, z, psfMag_r, modelMag_r, psfMag_g, modelMag_g, class
FROM PhotoObj
"""

data = SDSS.query_sql(query, data_release=19, timeout=300)
data.write("data/csv/raw_data.csv", format="csv", overwrite=True)
