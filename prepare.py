import os.path
import shutil

for year in range(2015, 2023 + 1):
    if not os.path.isdir(f"./{year}"):
        os.mkdir(f"./{year}")

    for day in range(1, 25 + 1):
        if not os.path.isdir(f"./{year}/day{day:02d}"):
            shutil.copytree("./base", f"./{year}/day{day:02d}")
            os.rename(f"./{year}/day{day:02d}/dayXX.py", f"./{year}/day{day:02d}/day{day:02d}.py")
