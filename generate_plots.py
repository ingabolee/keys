import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_plots():
    # Load data
    csv_path = 'data4.csv'
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    df = pd.read_csv(csv_path)
    df.columns = ['index', 'start', 'end', 'key', 'region']

    # Clean region data
    df_region_cleaned = df['region'].dropna()

    # --- Plot 1: 5% Bins ---
    bins_5 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    labels_5 = ['0-5', '6-10', '11-15', '16-20', '21-25', '26-30', '31-35', '36-40', '41-45', '46-50', 
                '51-55', '56-60', '61-65', '66-70', '71-75', '76-80', '81-85', '86-90', '91-95', '96-100']
    
    counts_5 = pd.cut(df_region_cleaned, bins=bins_5, labels=labels_5, right=True, include_lowest=True).value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    counts_5.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Frequency of Region Values (5% Bins)')
    plt.xlabel('Region Percentage Category')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('plot_5percent.png')
    plt.close()
    print("Saved plot_5percent.png")

    # --- Plot 2: 2.5% Bins ---
    bins_25 = [i * 2.5 for i in range(41)]
    labels_25 = [f"{bins_25[i]}-{bins_25[i+1]}" for i in range(40)]
    
    counts_25 = pd.cut(df_region_cleaned, bins=bins_25, labels=labels_25, right=True, include_lowest=True).value_counts().sort_index()

    plt.figure(figsize=(14, 7))
    counts_25.plot(kind='bar', color='salmon', edgecolor='black')
    plt.title('High-Resolution Frequency Analysis (2.5% Bins)')
    plt.xlabel('Region Percentage Category')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('plot_2_5percent.png')
    plt.close()
    print("Saved plot_2_5percent.png")

if __name__ == "__main__":
    generate_plots()
