#!/usr/bin/env python
"""Generate key figures and save to figures/ directory."""
import argparse, os
import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--results', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    # Placeholder Figure 3.2: activation bars
    labels = ['Riyadh','Dammam','Jeddah','Abha','Tabuk']
    activation = [24,24,13,13,18]
    plt.figure()
    plt.bar(labels, activation)
    plt.ylabel('NN activation (%)')
    plt.title('Hybrid Activation Frequencies (placeholder)')
    plt.savefig(os.path.join(args.out, 'fig_3_2_activation.pdf'), bbox_inches='tight')
    plt.close()

    # Placeholder Figure 2.1: simple text plot
    plt.figure()
    plt.text(0.1, 0.5, 'Workflow Diagram (placeholder)', fontsize=14)
    plt.axis('off')
    plt.savefig(os.path.join(args.out, 'fig_2_1_workflow.pdf'), bbox_inches='tight')
    plt.close()

    print("Figures saved (placeholders).")

if __name__ == '__main__':
    main()
