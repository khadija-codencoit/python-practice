from pathlib import Path

path = Path("Data_Strucure")

print("This is for exists : ",path.exists())
print("This is for file directory : ",path.is_file())

print(path.name)
print(path.stem)

array = []

for i in path.iterdir():
    print(i)
    if i.is_dir():
        array.append(i)

print(array)