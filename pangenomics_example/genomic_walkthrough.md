# Microbial Genome Data Mining For Comparative Genomics Walkthrough

---
## Get NCBI reports through web hooks

You can use `wget`, `curl`, etc. with the following NCBI urls to get the tabular datasets most 

Most curation, *Reference Genomes*:

- [reference prokaryote genomes]https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prok_reference_genomes.txt

Medium curation, *Representative Genomes*:

- [representative prokaryote genomes](https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prok_representative_genomes.txt)

Least curation, *Prokaryotes*: `https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt` 

- [latest prokaryote genomes](https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt)

---
## Pulling Data with Python

---
## Running the anvi'o pangenomics snakemake workflow

### Inputs 
	- Outputs from python data pulling  script: `*.fa`, `genome-analysis.txt`
	- anvi'o snakemake config file

### Outputs
	- anvi'o: Pangenome DB, 
---
