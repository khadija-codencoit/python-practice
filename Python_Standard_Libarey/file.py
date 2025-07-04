from pathlib import Path
from time import ctime
import shutil
import datetime

data = Path("Python_Standard_Libarey/paths_directory.py")
source = Path("sample.py")


# print(shutil.copy(data,source))

shutil.copyfile(data, source, follow_symlinks=True)
shutil.copymode(data, source, follow_symlinks=True)


# print(data.read_text())
# source.write_text(data.read_text())

# print(source.rename("kk"))
# source.rename("sample.py")
# print(source.exists())


# print(source.stat().st_ctime)
# print(ctime(source.stat().st_mtime))
# print(datetime.datetime.now())


# source.write_text()
# print(source.read_text())




