from pathlib import Path
from zipfile import ZipFile

with ZipFile("Zip1", "w") as z:
    for i in Path("Python_standard_libary").rglob("*"):
        z.write(i)
        
for z in ZipFile('Zip1', 'r').namelist():
    print(z)