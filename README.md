# Run a snakemake pipline on any HPC cluster

This [snakemake profile](https://snakemake.readthedocs.io/en/v7.3.8/executing/cli.html#profiles) configures a snakemke profile to run on almost any cluster system.

It takes the resources (threads, memory and time)  defined in the snakemake rules to prametrize the culster job submission.

I follow the somewhat standard resource keywords:
`mem_mb` and `time_min`. 
The mapping between  resources and cluster are defined in the `key_mapping.yaml`, allowing easy change of the parameters. For now We have mapping for Slurm, LSF amnd PBS ).

## automatic queue selection

If you have multiple queues on your system, list all queues available on your cluster in a table `queues.tsv` with the _maximum_ resource limitations. There is an example in `queues.tsv.example`. The wrapper then **automatically selects the optimal queue** for you. Fantastic, isn't it!?

Alternatively you can define/overwrite the queue values for all or some rules via the `cluster_config.yaml`.

Using this file you can also define `account` and
overwrite any other parameters defined using the config file.



## Use the profile

You need cookiecutter to be installed.

    conda install cookiecutter


To deploy this profile,

    mkdir -p ~/.config/snakemake
    cd ~/.config/snakemake
    cookiecutter https://github.com/Snakemake-Profiles/generic.git


Then, you can run your snakemake pipline on a cluster with

    snakemake <options> --profile cluster


If a job fails, you will find the "external jobid" in the error message.
You can investigate the job via this ID.
By default the cluster logs are saved in the folder `cluster_logs`

## Known issue with defautl ressources

Ideally one would also define standard resources in the profile but for now I encountered an error see https://github.com/snakemake/snakemake/issues/1186 .
