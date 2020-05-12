from PIL import Image
import os

def Setup(path, name):
    try:
        os.mkdir(path + "\\datapacks\\" + name)
    except:
        pass

    try:
        os.mkdir(path + "\\datapacks\\"+ name + "\\data")
    except:
        pass

    try:
        os.mkdir(path + "\\datapacks\\" + name + "\\data\\game")
    except:
        pass

    try:
        os.mkdir(path + "\\datapacks\\" + name + "\\data\\game\\functions")
    except:
        pass

    try:
        os.mkdir(path + "\\datapacks\\" + name +"\\data\\minecraft")
    except:
        pass

    try:
        os.mkdir(path + "\\datapacks\\" + name + "\\data\\minecraft\\tags")
    except:
        pass

    try:
        os.mkdir(path + "\\datapacks\\" + name +"\\data\\minecraft\\tags\\functions")
    except:
        pass

    file = open(path + "\\datapacks\\" + name + "\\data\\minecraft\\tags\\functions\\load.json","w")
    file.write("{\n  \"values\":[\n               \"game:load\"\n]\n}")
    file.close()

    file = open(path + "\\datapacks\\" + name + "\\data\\minecraft\\tags\\functions\\tick.json","w")
    file.write("{\n  \"values\":[\n               \"game:main\"\n  ]\n}")
    file.close()

    file = open(path + "\\datapacks\\" + name + "\\data\\game\\functions\\load.mcfunction","w")
    file.write("scoreboard players set @a PythonSleep 0")
    file.close()

    file = open(path + "\\datapacks\\" + name + "\\data\\game\\functions\\main.mcfunction","w")
    file.write("scoreboard objectives add PythonSleep dummy\nscoreboard players add @a PythonSleep 1\nexecute as @p at @s if score @s PythonSleep matches 1.. run reload")
    file.close()

    file = open(path + "\\datapacks\\" + name + "\\pack.mcmeta","w")
    file.write("{\n  \"pack\": {\n    \"pack_format\": 1,\n    \"description\": \"Python programm for " + name + "\"\n  }\n}")
    file.close()

    img = Image.new('RGB', (16,16), color = 'white')
    img.save(path + "\\datapacks\\" + name + "\\pack.png")
    #file = open(path + "\\datapacks\\" + name + "\\pack.png","w")
    #file.write("{\n  \"pack\": {\n    \"pack_format\": 1,\n    \"description\": #\"Python programm for " + name + "\"\n  }\n}")
    #file.close()

    #os.mkdir(path + "\\datapacks\\" + name + "\\data\\minecraft\\tags\\functions")
