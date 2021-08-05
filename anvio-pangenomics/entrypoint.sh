#!/bin/bash 

#source conda
source /opt/conda/etc/profile.d/conda.sh
#activate environment
conda activate anvioenv
#let process take the wheel
exec "$@"
