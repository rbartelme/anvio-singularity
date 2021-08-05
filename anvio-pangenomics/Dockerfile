FROM rbartelme/anvio-dbconfig:1

#install ncbi-genome-download via pip in anvioenv for easier pangenomics
RUN /opt/conda/envs/anvioenv/bin/pip install ncbi-genome-download

COPY entrypoint.sh ./
RUN chmod a+x entrypoint.sh

COPY profile .profile

ENTRYPOINT ["./entrypoint.sh"]
