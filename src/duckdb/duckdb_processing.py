import duckdb

def yield_training_batches(db_path, last_id, batch_size=10):

    conn = duckdb.connect(db_path)

    query = """
    SELECT *
    FROM processed_sdss_view
    ORDER BY id
    """

    result = conn.execute(query)

    while True:

        chunk = result.fetch_df_chunk(batch_size)

        if chunk.empty:
            break

        last_id = chunk["id"].max()

        X = chunk.drop(["target_class", "id"], axis=1)
        y = chunk["target_class"]

        yield X, y

    conn.close()
