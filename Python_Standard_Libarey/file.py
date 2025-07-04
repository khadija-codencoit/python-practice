from pathlib import Path
from time import ctime
import datetime

data = Path("paths_directory.py")
source = Path("sample.py")

# print(source.rename("kk"))
# source.rename("sample.py")
# print(source.exists())


# print(source.stat().st_ctime)
# print(ctime(source.stat().st_mtime))
# print(datetime.datetime.now())


# source.write_text()
# print(source.read_text())

print(data.read_text())