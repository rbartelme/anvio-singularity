# Running anvi'o in Singularity containers

Ryan Bartelme, PhD

---

## Preparation

If you want to test anvi'o on an HPC system, here are a few strategies:

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

***The latest docker image of anvi'o will **NOT** have the databases configured. This is also an opportune time to create your own customized docker image from the `meren/anvio:latest` docker image tag.*** 

---
## Making your own Dockerfile to customize your anvi'o runtime

See an example: [Dockerfile](anvio-dbconfig/Dockerfile) this runs through the database configurations for anvi'o. (As of 03-25-21 this does not properly compile the 3d structure db's)

---
## Configuring anvi'o Singularity containers
---
### Docker container image customization
In this case I used a [Dockerfile](anvio-pangenomics/Dockerfile), where I am building off the `anvio-dbconfig` [image](anvio-dbconfig/Dockerfile). The modifications include an installation of [ncbi-genome-download](https://github.com/kblin/ncbi-genome-download) using the anvio conda environment [pip](https://github.com/rbartelme/anvio-singularity/blob/bacaaec5130fdb188647c4cdac72aaa275e277b8/anvio-pangenomics/Dockerfile#L4) and setting the [entrypoint](anvio-pangenomics/entrypoint.sh) to the conda environment of anvio for the docker runtime. Note [profile](anvio-pangenomics/profile) is included to make sure the container sources the `.bashrc` for the conda path.

### Building Singularity images

Our local cluster singularity version:
```[rbartelme@gpu06 ~]$ singularity --version
singularity-ce version 3.8.0
```

**Building from the Docker image above:**

**NOTE:** *This required `sudo su` on our local cluster, which I have access to, this has not been tested with `--fakeroot` yet.*

`sudo su`

1. Singularity build statement, using Singularity [recipe](anvio-pangenomics/Singularity):

    `singularity build anvio-pangenomics.sif Singularity`

2. Get ownership of Singularity `*.sif` file and set group permissions.

    `sudo chown rbartelme:iplant-everyone anvio-pangenomics.sif`

3. Read up on job scheduling with your HPC's IT team documentation

---
## Example with SLURM, Singularity, and Snakemake

### Snakemake Workflows with Singularity

Anvi'o has awesome snakemake [workflows]() built in! This is the "end-to-end" approach for all your HPC or cloud compute needs. 

---

### Comparative Genomics

**Example json input for Comparative Genomics Workflow:**

---
