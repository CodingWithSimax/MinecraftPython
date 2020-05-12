import time

def run(text, path, name, f, p):
    #print(text)
    load = open(path + "\\datapacks\\" + name + "\\data\\game\\functions\\load.mcfunction","w")
    load.write(text + "\nscoreboard players set @a PythonSleep 1")
    load.close()
    Count = 0
    while True:
        f.seek(p)
        latest_data = f.read()
        p = f.tell()
        Count += 1
        if not latest_data == "":
            #print(latest_data)
            if latest_data.find("Reloading ResourceManager") > -1:
                print("Reloaded")
                break
        #if Count > 100:
        #    break

        #time.sleep(0.1)



    #print(text)
    load = open(path + "\\datapacks\\" + name + "\\data\\game\\functions\\load.mcfunction","w")
    load.write("scoreboard players set @a PythonSleep 1")
    load.close()
