import json
import random

with open("data.json") as fp:
    data = json.load(fp)

for year in range(2018, 2022):
    for month in range(1, 13):
        for day in range(1, 32):
            if random.randint(0, 3) == 0:
                if year not in data.keys():
                    data[year] = {}

                if month not in data[year].keys():
                    data[year][month] = {}

                data[year][month][day] = random.randint(0, 10)


with open("data.json", "w") as fp:
    json.dump(data, fp)
