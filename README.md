# Variant Table Analyzer (Python)
**Post-processing and summarization of annotated genetic variant tables**

## Overview

This repository contains a small Python project designed to automate the post-processing of annotated genetic variant tables, such as those produced by NGS pipelines and variant annotation tools.

After sequencing and variant calling, the typical output is a large table listing variants with information such as gene name, functional impact, and allele frequency. Before any biological interpretation, these tables must be filtered, organized, and summarized in a consistent and reproducible way.

This project implements a simple, transparent workflow that transforms a raw variant table into a gene-level summary focused on high-impact variants.

---

## What problem this addresses

In practical genomics and translational research workflows, variant annotation produces large tables that still require substantial manual post-processing to answer basic questions such as:

- Which genes accumulate more potentially severe variants?
- How many high-impact variants does each gene have?
- What is the average allele frequency of these variants per gene?

Although this step is rarely described in articles, it is a necessary intermediate layer between raw variant annotation and biological interpretation.

This project simulates and automates this post-processing step.

---

## What the script does

Given an annotated variant table, the script:

- Loads the variant table from CSV
- Converts the allele frequency column to numeric values
- Filters variants by functional impact (keeps only `high` impact variants)
- Groups results by gene
- Computes:
  - The number of high-impact variants per gene
  - The mean allele frequency (`mean_af`) per gene
- Merges these results into a summary table
- Saves the summary table to CSV
- Generates a simple bar plot showing the number of high-impact variants per gene

---

## Inputs and outputs

### Input

A CSV file with columns similar to:

- `sample_id`
- `gene`
- `variant`
- `impact`
- `af` (allele frequency)

Example file:

```
data/variants_example.csv
```

### Outputs

- `results_high_impact_by_gene.csv` — gene-level summary table
- `high_impact_variants_per_gene.png` — bar plot of high-impact variants per gene

---

## Project structure

```text
variant-table-analyzer/
├── data/
│   └── variants_example.csv
├── analyze_variants.py
├── results_high_impact_by_gene.csv
├── high_impact_variants_per_gene.png
└── README.md
```

---

## How to run

1. Install dependencies:

```bash
pip install pandas matplotlib
```

2. Run the script:

```bash
python analyze_variants.py
```

---

## What this project represents

This project demonstrates:

- Basic post-processing of NGS variant annotation results
- Data cleaning and type coercion
- Biological aggregation at the gene level
- Computation of simple summary statistics
- Automated generation of tables and plots
- Translation of a biological question into a small, reproducible data analysis script

This is intentionally a **simple and focused project**, meant to represent an early step in building structured and reproducible analysis workflows for genomics data.

---

## Notes

- This project uses a **small synthetic dataset** for demonstration purposes only.
- It does **not** perform clinical interpretation, pathogenicity classification, or real variant prioritization.
- Its goal is to demonstrate organization and summarization of results, not decision-making.

---

## Technologies used

- Python
- pandas
- matplotlib

---

## License

MIT License.
