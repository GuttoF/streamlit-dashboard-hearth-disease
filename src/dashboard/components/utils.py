from pathlib import Path

import duckdb
import pandas as pd


def load_processed_data() -> pd.DataFrame:
    db_path = (
        Path("pyproject.toml").resolve().parents[0]
        / "data"
        / "processed"
        / "db_processed.db"
    )
    print(db_path)
    with duckdb.connect(str(db_path)) as conn:
        data = conn.execute("SELECT * FROM heart_processed").fetchdf()

    data["sexo"] = data["sex"].map({1: "Masculino", 0: "Feminino"})
    data["tipo_dor_peito"] = data["chest_pain_type"].map(
        {
            1: "Angina típica",
            2: "Angina atípica",
            3: "Dor não-anginal",
            4: "Assintomático",
        }
    )

    return data
