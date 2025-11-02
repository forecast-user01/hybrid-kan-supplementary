# Data Access & Layout

This project uses **NASA POWER** hourly data (2018–2023) for five Saudi cities:
Riyadh, Dammam, Jeddah, Abha, Tabuk.

## Download

Use the script:
```bash
python code/scripts/fetch_nasa_power.py --cities riyadh dammam jeddah abha tabuk --start 2018-01-01 --end 2023-12-31 --out data/raw
```

Alternatively, download from NASA POWER web portal and place files under `data/raw/`.

## Structure
```
data/
  raw/                # raw CSVs from NASA POWER (one per city)
  processed/          # standardized, cleaned CSVs after preprocessing
```

## Notes
- No proprietary data in this repo.
- See manuscript for variable descriptions and preprocessing pipeline.
