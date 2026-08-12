from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw")

input_file = RAW_DIR / "ny_accidents.csv"

df = pd.read_csv(input_file)

CUTOFF = 20_000

for i in range(0, len(df), CUTOFF):
    part = df.iloc[i:i + CUTOFF]

    part_number = i // CUTOFF + 1

    output_file = RAW_DIR / f"dataset_part_{part_number}.csv"

    part.to_csv(output_file, index=False)

    print(f"Saved {output_file} with {len(part)} rows")
