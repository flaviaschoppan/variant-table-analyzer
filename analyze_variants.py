import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/variants_example.csv")

print(df.head())
print(df.info())

# Clean data
df["af"] = pd.to_numeric(df["af"], errors="coerce")

# Filter high impact variants
high_df = df[df["impact"] == "high"]

# Group by gene
counts = high_df.groupby("gene").size().reset_index(name="n_variants")

# Mean AF per gene
mean_af = high_df.groupby("gene")["af"].mean().reset_index(name="mean_af")

# Merge results
summary = pd.merge(counts, mean_af, on="gene")

print(summary)

# Save results
summary.to_csv("results_high_impact_by_gene.csv", index=False)

# Plot
plt.figure()
plt.bar(summary["gene"], summary["n_variants"])
plt.xlabel("Gene")
plt.ylabel("Number of high-impact variants")
plt.title("High-impact variants per gene")
plt.tight_layout()
plt.savefig("high_impact_variants_per_gene.png")
plt.show()
