import csv

import aiohttp
import asyncio


rawrzcookie_csvs = "https://raw.githubusercontent.com/rawrzcookie/TT2_CSV/main/csv"


async def download_file(filename):
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        async with session.get(f"{rawrzcookie_csvs}/{filename}.csv") as response:
            data = await response.text()
            return csv.reader(data.splitlines())


async def update_equipment():
    csv_file = await download_file("EquipmentSetInfo")

    with open("./tap_titans/models/player/model_type.py", "r") as fp:
        model_type_py = list(fp.read().splitlines())

    start = 0
    end = 0

    for x, line in enumerate(model_type_py):
        if "class EquipmentSets(" in line:
            start = x
        elif start and "\"" not in line:
            end = x
            break

    for line in csv_file:
        equipment_set = line[0]

        if any(equipment_set in i for i in model_type_py):
            continue

        model_type_py = [*model_type_py[:end], f'    {equipment_set} = "{equipment_set}"', *model_type_py[end:]]
        end += 1

    with open("./tap_titans/models/player/model_type.py", "w") as fp:
        fp.write("\n".join(model_type_py))


asyncio.run(update_equipment())
