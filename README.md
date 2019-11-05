# generic profile

This profile configures atlas to run on cluster system. The mapping between  ressources and cluster submission can be configured in the `key_mapping.yaml`.
In addition,  values can be overwritten by using the `overwrite_cluster_param.yaml`  file.

The units are minutes and GB but can be changed.


## Deploy profile

You would need cookiecutter to be installed.

    conda install cookiecutter

To deploy this profile,

    mkdir -p ~/.config/snakemake
    cd ~/.config/snakemake
    cookiecutter https://github.com/metagenome-atlas/clusterprofile.git


Then, you can run atlas on a cluster with

    atlas run <options> --profile cluster ...

so that jobs are submitted to the cluster.
If a job fails, you will find the "external jobid" in the error message.
You can investigate the job via this ID.
