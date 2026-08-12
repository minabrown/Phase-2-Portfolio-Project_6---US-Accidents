from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

files = sorted(RAW_DIR.glob("dataset_part_*.csv"))

dataframes = []

for file in files:
    df = pd.read_csv(file)
    dataframes.append(df)

combined_df = pd.concat(dataframes, ignore_index=True)

output_file = PROCESSED_DIR / "cleaned_ny_accidents.csv"

combined_df.to_csv(output_file, index=False)

print(f"Combined {len(files)} files")
print(f"Total rows: {len(combined_df)}")
print(f"Saved to: {output_file}")
