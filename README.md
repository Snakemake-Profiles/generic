# Run atlas on a cluster

This [snakemake profile](https://snakemake.readthedocs.io/en/stable/executable.html#profiles) configures atlas to run on cluster systems.

The resources (threads, memory and time) are defined in the atlas config file.
The mapping between  resources and cluster are defined in the `key_mapping.yaml`.
For now We have mapping for Slurm, LSF amnd PBS ).


If you need to define queues, accounts you can use this in the

In addition,  values can be overwritten by using the `cluster_config.yaml`  file.

The units are minutes and GB but can be changed.


## Deploy profile

You need cookiecutter to be installed.

    conda install cookiecutter

To deploy this profile,

    mkdir -p ~/.config/snakemake
    cd ~/.config/snakemake
    cookiecutter https://github.com/metagenome-atlas/clusterprofile.git


Then, you can run atlas on a cluster with

    atlas run <options> --profile cluster

so that jobs are submitted to the cluster.
If a job fails, you will find the "external jobid" in the error message.
You can investigate the job via this ID.
