import subprocess
import json
import pandas as pd
from pathlib import Path

# Dossier où sont stockés les résultats Hyperopt
results_dir = Path("user_data/hyperopt_results")
output_csv = "hyperopt_summary.csv"

rows = []

# Parcourt les fichiers d'hyperopt
for file in results_dir.glob("*.json"):
    print(f"Analyse de {file}")
    
    # Extrait les 3 meilleurs epochs (modifiable avec -n)
    # cmd = [ "docker", "run", "--rm",
    #     "freqtrade", "hyperopt-show",
    #     "--print-json",
    #     "--hyperopt-filename", str(file),
    #     "-n", "3"   # top 3 résultats par fichier
    # ]
    # result = subprocess.run(cmd, capture_output=True, text=True)
    # print(result.stdout)
    
    try:
        # data = json.loads(result.stdout)
        print(f"Lecture de {file}")
        print(file.read_text()[:200])  # affiche les 200 premiers caractères
        data = json.loads(file.read_text())
        print(data)
        # peut être liste ou dict selon la version
        if isinstance(data, dict):
            data = [data]
        for d in data:
            rows.append({
                "file": file.name,
                "epoch": d.get("epoch"),
                "objective": d.get("loss"),
                "profit_pct": d.get("total_profit_pct"),
                "cagr": d.get("cagr"),
                "sharpe": d.get("sharpe"),
                "sortino": d.get("sortino"),
                "calmar": d.get("calmar"),
                "max_drawdown": d.get("max_drawdown"),
                "trades": d.get("total_trades"),
                "profit_factor": d.get("profit_factor"),
                "expectancy": d.get("expectancy"),
            })
    except json.JSONDecodeError as e:
        print(f"⚠️ Impossible de parser {file}: {e}")

# Création DataFrame
df = pd.DataFrame(rows)
df = df.sort_values(by="profit_pct", ascending=False)

# Sauvegarde CSV
df.to_csv(output_csv, index=False)
print(f"Résumé sauvegardé dans {output_csv}")

print(df.head(10))  # affiche les 10 meilleurs
