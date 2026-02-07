import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
with open("events.json", "r") as f:
    events = json.load(f)
    df = pd.DataFrame(events["events"])
    plt.figure(figsize=(10, 10))
    sns.countplot(data=df, x="signature", palette='inferno')
    plt.ylabel("Кол-во инцидентов")
    plt.xlabel("Имя сигнатуры")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()