#!/usr/bin/env bash
set -e

CITIES="riyadh dammam jeddah abha tabuk"

python code/scripts/fetch_nasa_power.py --cities $CITIES --start 2018-01-01 --end 2023-12-31 --out data/raw
python code/scripts/preprocess.py --in data/raw --out data/processed
python code/scripts/train_models.py --data data/processed --out results --cities $CITIES
python code/scripts/evaluate.py --data data/processed --models results/checkpoints --out results/metrics
python code/scripts/plot_figures.py --results results --out figures

echo "End-to-end pipeline completed."
