# Running anvi'o in Singularity containers

Ryan Bartelme, PhD

---

## Preparation

### Pulling anvi'o docker image into Singularity

**Start by using singularity to pull the latest version of the anvi'o image from dockerhub:**

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

The latest docker image of anvi'o will **NOT** have the databases configured. This is also an opportune time to design an experiment by creating your own docker image from the `meren/anvio:latest` docker image tag. 

---
## Making your own Dockerfile to modify anvi'o

See an example: [Dockerfile](anvio-dbconfig/Dockerfile) this runs through the database configurations for anvi'o. (As of 03-25-21 this does not properly compile the 3d structure db's)

---

## Snakemake Workflows with Singularity

Anvi'o has awesome snakemake workflows built in! This is the "end-to-end" approach for all your HPC or cloud compute needs. 

---

### Metagenomics

**Running Snakemake Metagenomics workflow:**
Steps:
1. Execute Singularity Command
2. That's it.


`anvi-run-workflow -w metagenomics-workflow --get-default-config metagenomics-default.json`

Now you can open the json file to edit the metagenomics workflow parameters to suit your analysis.

Run the analysis and save the graph of the workflow.
`anvi-run-workflow -w metagenomics-workflow -c metagenomics.json --save-workflow-graph`



---

### Comparative Genomics

**Example json input for Comparative Genomics Workflow:**

---
