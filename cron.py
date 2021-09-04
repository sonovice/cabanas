#!/usr/bin/python3

import json
import subprocess
import sys
from datetime import datetime

INTERFACE = sys.argv[1]

now = datetime.now()
year = str(now.year)
month = str(now.month)
day = str(now.day)

with open("data.json") as fp:
    data = json.load(fp)

if year not in data.keys():
    data[year] = {}

if month not in data[year].keys():
    data[year][month] = {}

if day not in data[year][month].keys():
    data[year][month][day] = []

response = subprocess.run(
    f"iw dev {INTERFACE} station dump | grep 'Station' | awk '{{print $2}}'",
    shell=True,
    capture_output=True,
)
macs = response.stdout.decode("utf-8").strip().split("\n")
for mac in macs:
    if mac not in data[year][month][day]:
        data[year][month][day].append(mac)

with open("data.json", "w") as fp:
    json.dump(data, fp)
