# generic profile

This profile configures snakemake to run on any cluster system. The mapping between snakemake ressources and cluster submission can be configured in the `key_mapping.yaml`.
In addition,  values can be overwritten by using the `overwrite_cluster_param.yaml`  file.

The units are minutes and GB but can be changed.


## Deploy profile

To deploy this profile,

    mkdir -p ~/.config/snakemake
    cd ~/.config/snakemake
    cookiecutter https://github.com/Snakemake-Profiles/generic.git


Then, you can run Snakemake with

    snakemake --profile cluster ...

so that jobs are submitted to the cluster.
If a job fails, you will find the "external jobid" in the Snakemake error message.
You can investigate the job via this ID.
