import zipfile
import json
import pandas as pd

# === FILE PATHS ===
indicator_file = "user_data/analysis/ichimoku_rebond_entries.csv"
merged_output = "user_data/analysis/merged_trades.csv"
corr_output = "user_data/analysis/indicator_loss_correlation.csv"

# === GET LATEST BACKTEST ZIP FILE ===
last_result_path = "user_data/backtest_results/.last_result.json"
with open(last_result_path, 'r') as f:
    last_result = json.load(f)
    
zip_filename = last_result["latest_backtest"]
zip_path = f"user_data/backtest_results/{zip_filename}"

# Extract the base name without extension for the trades file path
base_name = zip_filename.replace('.zip', '')
trades_file_path = f"{base_name}.json"

print(f"[+] Using backtest file: {zip_path}")
print(f"[+] Looking for trades file: {trades_file_path}")

# === LOAD INDICATOR ENTRIES ===
indicators_df = pd.read_csv(indicator_file, index_col=0)  # Use first column as index
indicators_df["date"] = pd.to_datetime(indicators_df["date"])

# === LOAD TRADES.JSON FROM ZIP ===
with zipfile.ZipFile(zip_path, 'r') as z:
    with z.open(trades_file_path) as f:
        trades_data = json.load(f)

# Extract the actual trades list from the data structure
trades_list = None
if isinstance(trades_data, dict):
    # Check strategy section first (this is where the actual trades list is located)
    if 'strategy' in trades_data and isinstance(trades_data['strategy'], dict):
        strategy_data = trades_data['strategy']
        # Find the first strategy that has trades
        for strategy_name, strategy_content in strategy_data.items():
            if isinstance(strategy_content, dict) and 'trades' in strategy_content:
                trades_list = strategy_content['trades']
                if isinstance(trades_list, list):  # Make sure it's a list, not just a count
                    print(f"[+] Found {len(trades_list)} trades in strategy '{strategy_name}'")
                    break
    
    # Fallback to other locations
    if trades_list is None and 'trades' in trades_data:
        trades_list = trades_data['trades']

if trades_list is None or not isinstance(trades_list, list):
    raise ValueError("Could not find trades data (as a list) in the loaded JSON structure")

trades_df = pd.DataFrame(trades_list)
trades_df.to_csv("user_data/analysis/all_trades.csv", index=False)

# Ensure correct datetime format and timezone consistency
trades_df["open_date"] = pd.to_datetime(trades_df["open_date"]).dt.tz_localize(None)  # Remove timezone
indicators_df["timestamp"] = pd.to_datetime(indicators_df["timestamp"]).dt.tz_localize(None)  # Remove timezone

# Ensure indicators date is also timezone-naive (if it has timezone info)
if indicators_df["date"].dt.tz is not None:
    indicators_df["date"] = indicators_df["date"].dt.tz_localize(None)

# === MERGE ===
merged_df = pd.merge(
    trades_df,
    indicators_df,
    left_on=["pair", "open_date"],
    right_on=["pair", "timestamp"],
    how="inner"
)

# Transform all boolean columns to int
bool_cols = merged_df.select_dtypes(include=["bool"]).columns
merged_df[bool_cols] = merged_df[bool_cols].astype(int)

# === ADD LOSS FLAG ===
merged_df["is_loss"] = (merged_df["profit_abs"] < 0).astype(int)

# === SAVE MERGED DATASET ===
merged_df.to_csv(merged_output, index=False)
print(f"[+] Merged dataset saved to {merged_output}")

# === CORRELATION ANALYSIS ===
# Select only numeric columns
numeric_cols = merged_df.select_dtypes(include=["number"]).columns.tolist()

# Exclude target itself
if "is_loss" in numeric_cols:
    numeric_cols = ["adx"]

correlations = {}
for col in numeric_cols:
    corr = merged_df["is_loss"].corr(merged_df[col])
    correlations[col] = corr

# Convert to DataFrame
corr_df = pd.DataFrame(list(correlations.items()), columns=["indicator", "correlation_with_loss"])
corr_df = corr_df.sort_values(by="correlation_with_loss", ascending=False)

# Save correlations
corr_df.to_csv(corr_output, index=False)
print(f"[+] Correlations saved to {corr_output}")

# Preview
print("\nTop correlated indicators with losing trades:")
print(corr_df.head(10))
