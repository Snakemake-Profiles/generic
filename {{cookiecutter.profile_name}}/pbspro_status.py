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

    jsondoc = json.loads(res.stdout.decode())
    job_state = jsondoc["Jobs"][jobid]["job_state"]

    if job_state == "C":
        exit_status = jsondoc["Jobs"][jobid]["Exit_status"]
        if exit_status == "0":
            print("success")
        else:
            print("failed")
    else:
        print("running")

except (subprocess.CalledProcessError, IndexError, KeyboardInterrupt) as e:
    print("failed")
