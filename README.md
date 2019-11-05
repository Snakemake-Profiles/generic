# Run atlas on a cluster

This [snakemake profile](https://snakemake.readthedocs.io/en/stable/executable.html#profiles) configures atlas to run on cluster systems.

The resources (threads, memory and time) are defined in the atlas config file.
The units are minutes and GB but can be changed. The mapping between  resources and cluster are defined in the `key_mapping.yaml`. For now We have mapping for Slurm, LSF amnd PBS ).


If you need to define queues, accounts you can do this for all rules or for specific rules in the `cluster_config.yaml`

In addition, using this file you can overwrite the resources defined using the config file.




## Use the profile

You need cookiecutter to be installed.

    conda install cookiecutter

You should know what the default queue/partition you are using.

To deploy this profile,

    mkdir -p ~/.config/snakemake
    cd ~/.config/snakemake
    cookiecutter https://github.com/metagenome-atlas/clusterprofile.git


Then, you can run atlas on a cluster with

    atlas run <options> --profile cluster


If a job fails, you will find the "external jobid" in the error message.
You can investigate the job via this ID.
