#!/bin/bash 

#activate environment
conda activate anvioenv
#let process take the wheel
exec "$@"
