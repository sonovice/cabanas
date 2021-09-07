import json
import random

with open("data.json") as fp:
    data = json.load(fp)

for year in range(2018, 2022):
    for month in range(1, 13):
        for day in range(1, 32):
            if random.randint(0, 3) == 0:
                for _ in range(random.randint(0, 10)):
                    mac = ":".join(
                        map(
                            lambda x: "%02x" % x, random.sample(range(0, 256), 6)
                        )
                    )

                    if year not in data.keys():
                        data[year] = {}

                    if month not in data[year].keys():
                        data[year][month] = {}

                    if day not in data[year][month].keys():
                        data[year][month][day] = []

                    if mac not in data[year][month][day]:
                        data[year][month][day].append(mac)

with open("data.json", "w") as fp:
    json.dump(data, fp)
