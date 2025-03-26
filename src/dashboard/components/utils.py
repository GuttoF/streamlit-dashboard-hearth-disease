from pathlib import Path

import duckdb
import pandas as pd


def load_processed_data() -> pd.DataFrame:
    db_path = Path(__file__).parents[3] / "data" / "processed" / "db_processed.db"
    with duckdb.connect(str(db_path)) as conn:
        return conn.execute("SELECT * FROM heart_processed").fetchdf()


def load_interim_data() -> pd.DataFrame:
    db_path = Path(__file__).parents[3] / "data" / "interim" / "db.db"
    with duckdb.connect(str(db_path)) as conn:
        return conn.execute("SELECT * FROM heart").fetchdf()
