file = open(r"C:\Users\simon\AppData\Roaming\.minecraft\saves\PythonTest\datapacks\Dies hier ist ein Test Datapack\pack.mcmeta").read().split("\n")

newfile = ""

for i in file:
    if newfile == "":
        newfile += i

    else:
        newfile += "\\n" + i

print(newfile)
