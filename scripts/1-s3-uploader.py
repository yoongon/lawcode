import os
import time
import datetime
import subprocess


def get_date():
    return str(datetime.datetime.fromtimestamp(time.time()).date())


def run_cmd(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    res = process.communicate()[0].decode("utf-8")
    if process.returncode != 0:
        return '', False
    return res.strip(), True


if __name__ == '__main__':
    filename = 'hello.file'
    cmd = 'aws s3 cp draw/{} s3://lawcode/{}-{}'.format(filename, filename, get_date())
    print(cmd)
