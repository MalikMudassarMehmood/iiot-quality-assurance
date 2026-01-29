import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# === File paths ===
input_file = r'D:\Python\Water_Bottle_dataset.xlsx'
output_file = r'D:\Python\Water_Bottle_dataset_Processed.xlsx'

# === Load Excel file ===
df = pd.read_excel(input_file, engine='openpyxl')

# === Validation ===
if df.shape[1] < 9:
    raise ValueError("The Excel file must have at least 9 columns.")

# === Add result and timing columns ===
df['Step 1 Result'] = ''
df['Step 2 Result'] = ''
df['Step 3 Result'] = ''
df['Step 1 Time (ms)'] = 0.0
df['Step 2 Time (ms)'] = 0.0
df['Step 3 Time (ms)'] = 0.0

# === Process each row with timing ===
for index, row in df.iterrows():
    # Step 1: Empty Bottle
    start1 = time.perf_counter()
    col1, min1, max1 = row[0], row[1], row[2]
    if min1 <= col1 <= max1:
        df.at[index, 'Step 1 Result'] = 'ACCEPT'
    else:
        df.at[index, 'Step 1 Result'] = 'REJECT'
        df.at[index, 'Step 1 Time (ms)'] = (time.perf_counter() - start1) * 1000
        continue
    df.at[index, 'Step 1 Time (ms)'] = (time.perf_counter() - start1) * 1000

    # Step 2: Filled Bottle
    start2 = time.perf_counter()
    col4, min2, max2 = row[3], row[4], row[5]
    if min2 <= col4 <= max2:
        df.at[index, 'Step 2 Result'] = 'ACCEPT'
    else:
        df.at[index, 'Step 2 Result'] = 'REJECT'
        df.at[index, 'Step 2 Time (ms)'] = (time.perf_counter() - start2) * 1000
        continue
    df.at[index, 'Step 2 Time (ms)'] = (time.perf_counter() - start2) * 1000

    # Step 3: Final Product
    start3 = time.perf_counter()
    col7, min3, max3 = row[6], row[7], row[8]
    if min3 <= col7 <= max3:
        df.at[index, 'Step 3 Result'] = 'ACCEPT'
    else:
        df.at[index, 'Step 3 Result'] = 'REJECT'
    df.at[index, 'Step 3 Time (ms)'] = (time.perf_counter() - start3) * 1000

# === Save processed data ===
df.to_excel(output_file, index=False)
print(f"✅ Processing complete. Results saved to: {output_file}")

# ======== Summary Stats ========
step1_rejects = df['Step 1 Result'].value_counts().get('REJECT', 0)
step2_rejects = df['Step 2 Result'].value_counts().get('REJECT', 0)
step3_rejects = df['Step 3 Result'].value_counts().get('REJECT', 0)

step1_accepts = df['Step 1 Result'].value_counts().get('ACCEPT', 0)
step2_accepts = df['Step 2 Result'].value_counts().get('ACCEPT', 0)
step3_accepts = df['Step 3 Result'].value_counts().get('ACCEPT', 0)

fully_accepted = df[
    (df['Step 1 Result'] == 'ACCEPT') &
    (df['Step 2 Result'] == 'ACCEPT') &
    (df['Step 3 Result'] == 'ACCEPT')
].shape[0]

# ======== Average time per step ========
avg_times = [
    df['Step 1 Time (ms)'].mean(),
    df['Step 2 Time (ms)'].mean(),
    df['Step 3 Time (ms)'].mean()
]

labels = ['Empty Bottle', 'Filled Bottle', 'Final Product']

# === Threshold Ranges for each step ===
min_values = [
    df.iloc[0, 1],  # Step 1 Min
    df.iloc[0, 4],  # Step 2 Min
    df.iloc[0, 7],  # Step 3 Min
]

max_values = [
    df.iloc[0, 2],  # Step 1 Max
    df.iloc[0, 5],  # Step 2 Max
    df.iloc[0, 8],  # Step 3 Max
]

# ==== Plot 1: Accept vs Reject counts ====
x = np.arange(len(labels))
bar_width = 0.35

accepts = [step1_accepts, step2_accepts, step3_accepts]
rejects = [step1_rejects, step2_rejects, step3_rejects]

plt.figure(figsize=(10,6))
plt.bar(x - bar_width/2, accepts, bar_width, label='ACCEPT', color='#2ecc71', edgecolor='black')
plt.bar(x + bar_width/2, rejects, bar_width, label='REJECT', color='#e74c3c', edgecolor='black')

plt.xticks(x, labels)
plt.ylabel('Number of Bottles')
plt.title('Bottle Acceptance and Rejection at Each Step')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.subplots_adjust(bottom=0.25)  # Add space for min/max text below

# Display counts and thresholds
for i in range(len(labels)):
    # Bar value labels
    plt.text(x[i] - bar_width/2, accepts[i] + 2, str(accepts[i]), ha='center', fontweight='bold')
    plt.text(x[i] + bar_width/2, rejects[i] + 2, str(rejects[i]), ha='center', fontweight='bold')

    # Thresholds BELOW x-axis
    plt.text(x[i], -max(accepts + rejects) * 0.07,
             f"Min: {min_values[i]}\nMax: {max_values[i]}",
             ha='center', va='top', fontsize=9, color='black', fontweight='bold')

plt.tight_layout()
plt.show()

# ==== Plot 2: Average processing time per step ====
plt.figure(figsize=(10,6))
plt.bar(labels, avg_times, color='#3498db', edgecolor='black')
plt.ylabel('Average Time (ms)')
plt.title('Average Processing Time per Step')
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(avg_times):
    plt.text(i, v + 0.001, f"{v:.4f}", ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

# ==== Plot 3: Average processing time per step in 1000-row chunks ====
chunk_size = 1000
num_chunks = (len(df) + chunk_size - 1) // chunk_size

chunk_labels = []
step1_avg_chunk = []
step2_avg_chunk = []
step3_avg_chunk = []

for i in range(num_chunks):
    start_idx = i * chunk_size
    end_idx = min((i + 1) * chunk_size, len(df))
    chunk_df = df.iloc[start_idx:end_idx]

    chunk_labels.append(f'{start_idx+1}-{end_idx}')
    step1_avg_chunk.append(chunk_df['Step 1 Time (ms)'].mean())
    step2_avg_chunk.append(chunk_df['Step 2 Time (ms)'].mean())
    step3_avg_chunk.append(chunk_df['Step 3 Time (ms)'].mean())

x = np.arange(num_chunks)
bar_width = 0.25

plt.figure(figsize=(14,7))
plt.bar(x - bar_width, step1_avg_chunk, width=bar_width, label='Step 1 Time', color='#1f77b4')
plt.bar(x, step2_avg_chunk, width=bar_width, label='Step 2 Time', color='#ff7f0e')
plt.bar(x + bar_width, step3_avg_chunk, width=bar_width, label='Step 3 Time', color='#2ca02c')

plt.xlabel('Total Bottles')
plt.ylabel('Average Time (ms)')
plt.title(f'Average Processing Time per Step for Each {chunk_size} Rows')
plt.xticks(x, chunk_labels, rotation=45, ha='right')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ======== Console Summary ========
print("\n--- SUMMARY ---")
print(f"Empty Bottle: {step1_accepts} Accepted, {step1_rejects} Rejected")
print(f"Filled Bottle: {step2_accepts} Accepted, {step2_rejects} Rejected")
print(f"Final Product: {step3_accepts} Accepted, {step3_rejects} Rejected")
print(f"✅ Fully Accepted Bottles: {fully_accepted}")
print(f"\nAverage Step Times (ms):")
print(f" Step 1: {avg_times[0]:.6f} ms")
print(f" Step 2: {avg_times[1]:.6f} ms")
print(f" Step 3: {avg_times[2]:.6f} ms")

print("\nThreshold Ranges:")
for i, label in enumerate(labels):
    print(f" {label}: Min = {min_values[i]}, Max = {max_values[i]}")
