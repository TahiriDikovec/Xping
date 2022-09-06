import os
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("target")
args = parser.parse_args()

ifconfig = subprocess.check_output("ifconfig | grep 10.10. | awk '{print $2}'", shell=True).strip()

myIP = ifconfig.decode()
target = args.target

command = 'ping ' + target + ' | while read ping; do echo "' + myIP + ' -> $ping - $(date)"; done'

os.system(command)
