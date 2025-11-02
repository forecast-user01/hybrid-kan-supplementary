#!/usr/bin/env python
"""Preprocess raw NASA POWER CSVs, compute features, and standardize."""
import argparse, os, pandas as pd

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='inp', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    # Placeholder loop
    for fn in os.listdir(args.inp):
        if fn.endswith('.csv'):
            df = pd.read_csv(os.path.join(args.inp, fn))
            # TODO: add feature engineering & normalization
            df.to_csv(os.path.join(args.out, fn.replace('.csv','_processed.csv')), index=False)
    print("Preprocessing placeholders done.")

if __name__ == "__main__":
    main()
