#!/usr/bin/env python3

import sys
import subprocess
import json

jobid = sys.argv[1]

try:
    res = subprocess.run(
        "qstat -f -F json -x {}".format(jobid),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    tracejob = subprocess.run(
        "tracejob -n 1 {}".format(jobid),
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True
    )

    jsondoc = json.loads(res.stdout.decode())
    job_state = jsondoc["Jobs"][jobid]["job_state"]

    if job_state:
        print("running")
    else:
        exit_status_0 = "Exit_status=0" in tracejob.stdout
        if exit_status_0:
            print("success")
        else:
            print("failed")

except (subprocess.CalledProcessError, IndexError, KeyboardInterrupt) as e:
    print("failed")
