FROM meren/anvio

#configure anvi'o databases inside container environment
RUN anvi-setup-ncbi-cogs --just-do-it 
RUN anvi-setup-interacdome --force
#RUN anvi-setup-pdb-database --force
RUN anvi-setup-trna-taxonomy --force
RUN anvi-setup-kegg-kofams --just-do-it
RUN anvi-setup-pfams --force
RUN anvi-setup-scg-taxonomy --force
