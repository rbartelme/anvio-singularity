#!/usr/bin/env python3

# import packages
from Bio import Entrez
# input organism id from cli flag as an array

    #define test for array input
    #function to query ncbi by tax id

#Input email address for Entrez as string

    #define test for email string input
    #assign string email

#NCBI setup
Entrez.email = email


# define function to get fasta & metadata for all that match the ncbi organism id
rec = Entrez.read(Entrez.esearch(db="genome", term="%s.%s"%(acc,ver) ))

# get human readable spcies names for each result
    
# sub `_` for whitespace in organism names

# pull associated fasta and metadata

# write out ncbi metadata for downstream analyses

# write out anvi'o snakemake tsv input format i.e. organism_name_here`\t`fasta_file_here.fa

    
