#!/bin/sh

#SBATCH --job-name=firstjob          # Job name
#SBATCH --nodes=1                    # Number of nodes
#SBATCH --ntasks-per-node=1          # Number of tasks per node
#SBATCH --partition=cpu              # Partition
#SBATCH --mem-per-cpu=1024           # Memory per processor
#SBATCH --time=00:05:00              # Time limit hrs:min:sec
#SBATCH --output=%N.%j.out           # Standard output and error log
#SBATCH --error=%N.%j.err

python /home/wladimir.banda/UNIT2-examples/example.py
