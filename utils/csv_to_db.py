from pathlib import Path

import duckdb
import pandas as pd


def convert_csv_to_db() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    csv_path = project_dir / "data" / "raw" / "heart.csv"
    db_path = project_dir / "data" / "interim" / "db.db"

    db_path.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(csv_path)

    conn = duckdb.connect(str(db_path))
    conn.register("df_temp", df)
    conn.execute("CREATE TABLE heart AS SELECT * FROM df_temp")
    conn.close()

    print(f"Data stored in: {db_path}")


if __name__ == "__main__":
    convert_csv_to_db()
