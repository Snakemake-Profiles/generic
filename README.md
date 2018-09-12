# adaptable profile

This profile configures snakemake to run on any cluster system. The mapping between snakemake ressources and cluster submission can be configured.  


## Deploy profile

To deploy this profile,

    mkdir -p ~/.config/snakemake
    cd ~/.config/snakemake
    cookiecutter https://github.com/silask/adaptable_profile.git


Then, you can run Snakemake with

    snakemake --profile surfsara-grid ...

so that jobs are submitted to the grid.
If a job fails, you will find the "external jobid" in the Snakemake error message.
You can investigate the job via this ID.
