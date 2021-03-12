# Running anvi'o in Singularity containers

Ryan Bartelme, PhD

---

## Preparation

### Pulling anvi'o docker image into Singularity

**Start by using singularity to pull the image from dockerhub:**

```bash
singularity pull docker://meren/anvio
```

**After seeing the standard output of the docker pull command, Singularity will print out something like:**
```bash
INFO:    Creating SIF file...
```

**And the `*.sif` file should appear in the directory:**
```
$ ls
anvio_latest.sif
```

---

## Snakemake Workflows with Singularity

Anvi'o has awesome snakemake workflows built in! This is the "end to end" approach for all your HPC or cloud compute needs.

### Metagenomics

**Example json input for Metagenomics Workflow:**

### Comparative Genomics

**Example json input for Comparative Genomics Workflow:**

---

## Executing single anvi'o processes

Certain processes in anvi'o are computationally intensive, and others are not. Maybe you are interested in writing bash scripts to execute your anvi'o software needs. This section is for that kind of user. 

### Ex 1

### Ex 2

---
