#!/usr/bin/env python3


import sys
from subprocess import Popen, PIPE

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


# let snakemake read job_properties
from snakemake.utils import read_job_properties



jobscript = sys.argv[1]
job_properties = read_job_properties(jobscript)

#default paramters defined in cluster_spec (accessed via snakemake read_job_properties)
cluster_param= job_properties["cluster"]

if job_properties["type"]=='rule':
    cluster_param['name'] = job_properties['rule']
elif job_properties["type"]=='group':
    cluster_param['name'] = job_properties['groupid']
else:
    raise NotImplementedError(f"Don't know what to do with job_properties['type']=={job_properties['type']}")


# overwrite default parameters if defined in rule (or config file)
if 'threads' in job_properties:
    cluster_param["threads"] = job_properties["threads"]
for res in ['time','mem']:
    if res in job_properties["resources"]:
        cluster_param[res] = job_properties["resources"][res]

# time in hours
if "time" in cluster_param:
    cluster_param["time"]*=60


# check which system you are on and load command command_options

command_options= cluster_param['command_options'][cluster_param['system']]
command= command_options['command']

key_mapping= command_options['key_mapping']

# construct command:
for  key in key_mapping:
    if key in cluster_param:
        command+=" "
        command+=key_mapping[key].format(cluster_param[key])

command+=' {}'.format(jobscript)

eprint("submit command: "+command)

p = Popen(command.split(' '), stdout=PIPE, stderr=PIPE)
output, error = p.communicate()
if p.returncode != 0:
    raise Exception("Job can't be submitted\n"+output.decode("utf-8")+error.decode("utf-8"))
else:
    res= output.decode("utf-8")
    jobid= int(res.strip().split()[-1])
    print(jobid)
