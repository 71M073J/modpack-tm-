import os

#for file in os.listdir("Downloads"):
#    if file.endswith(".jar"):
#        os.rename("Downloads/" + file, "Downloads/_" + file)
dire = "C:/Users/timotej/AppData/Roaming/.minecraft/1.18modpack/mods"
for file in os.listdir(dire):
    if file.endswith(".jar"):
        print(file)
        if file.startswith("_"):
            noun = file[1:]
            file = dire + "/" + file
            try:
                os.rename(file, dire + "/" + noun)
            except FileExistsError:
                os.remove(file)