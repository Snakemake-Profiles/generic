# adaptable profile

This profile configures snakemake to run on any cluster system. The mapping between snakemake ressources and cluster submission can be configured in the cluster_spec.yaml.
In addition, default values are used for all rules not having the snakemake ressource paremeters.

The units are minutes and GB but can be changed.


## Deploy profile

To deploy this profile,

    mkdir -p ~/.config/snakemake
    cd ~/.config/snakemake
    cookiecutter https://github.com/silask/adaptable_profile.git


Then, you can run Snakemake with

    snakemake --profile adaptable_profile ...

so that jobs are submitted to the cluster.
If a job fails, you will find the "external jobid" in the Snakemake error message.
You can investigate the job via this ID.
