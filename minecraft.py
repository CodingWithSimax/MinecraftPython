

import runcommand
#from setup import Setup
import os

from os import walk

from PIL import Image

from setup import Setup
#command.run("say hi")




class cmd:
    def __init__(self,path, datapackname):
        self.path = path
        self.name = datapackname
        Setup(path, self.name)

        self.minecraftpath = ""

        for i in path.split("\\"):
            if i == ".minecraft":
                self.minecraftpath += "\\.minecraft"
                break
            else:
                if self.minecraftpath == "":
                    self.minecraftpath += i
                else:
                    self.minecraftpath += "\\" + i

        print(self.minecraftpath)
        self.p = 0
        self.f = open(self.minecraftpath + "\\logs\\latest.log")

        class BlockTypes:
            def __init__(self):
                self.wool = ["white_wool", "orange_wool", "magenta_wool", "light_blue_wool","yellow_wool","lime_wool","pink_wool","gray_wool", "light_gray_wool","cyan_wool","purple_wool","blue_wool","brown_wool","green_wool","red_wool","black_wool"]
                self.concrete = ["white_concrete", "orange_concrete", "magenta_concrete", "light_blue_concrete","yellow_concrete","lime_concrete","pink_concrete","gray_concrete", "light_gray_concrete","cyan_concrete","purple_concrete","blue_concrete","brown_concrete","green_concrete","red_concrete","black_concrete"]
                self.terracotta = ["white_terracotta", "orange_terracotta", "magenta_terracotta", "light_blue_terracotta","yellow_terracotta","lime_terracotta","pink_terracotta","gray_terracotta", "light_gray_terracotta","cyan_terracotta","purple_terracotta","blue_terracotta","brown_terracotta","green_terracotta","red_terracotta","black_terracotta"]

                self.planks = ["oak_planks", "spruce_planks", "birch_planks","jungle_planks","acacia_planks","dark_oak_planks"]

                self.materials = ["emerald_block",  "gold_block", "iron_block","diamond_block","lapis_block"]

                self.all = [*self.wool,*self.concrete,*self.terracotta,*self.planks,*self.materials]

        self.types = BlockTypes()

        self.run("reload")

    def newdata(self):
        self.f.seek(self.p)
        latest_data = self.f.read()
        self.p = self.f.tell()
        return latest_data



    def run(self,command):
        self.newdata()
        runcommand.run(command, self.path, self.name, self.f, self.p)


    def sayInChat(self,text):
        self.newdata()
        runcommand.run("say " + text, self.path, self.name, self.f, self.p)




    def get_chat(self):
        data = self.newdata()
        newchat = []
        for g in data.split("\n"):
            if not g == "":
                if g.split(" ")[1] == "[main/INFO]:" and g.split(" ")[2] == "[CHAT]" and g.split(" ")[3].find("<") > -1 and g.split(" ")[3].find(">") > -1:
                    if True:
                        #print(g.split(" ")[3].split("<")[1].split("> ")[1])
                        newchat.append([g.split(" ")[3].split("<")[1].split(">")[0], g.split("<")[1].split("> ")[1]])

            #except:
            #    pass

        return newchat

    def build_image(self,imgpath, blockposition, ABlocks,TexturePath , scale = 1, direction="x", Fast=False):
        #AllowedBlocks = open("blocklist.txt").read().split("\n")
        TexturePath = TexturePath + "\\assets\\minecraft\\textures\\block\\"

        AllowedBlocks = []

        for i in ABlocks:
            if type(i) is list:
                for i in i:
                    AllowedBlocks.append(i)

            else:
                AllowedBlocks.append(i)



        BlockColors = []

        for i in AllowedBlocks:
            if not i == "":
                f = []
                for (dirpath, dirnames, filenames) in walk(TexturePath):
                    f.extend(filenames)
                    break


                for g in f:
                    if g.find(i) > -1:
                        img = Image.open(TexturePath + g)
                        size = img.size

                        Count = 0

                        Colors = []

                        for x in range(0,size[0]):
                            for y in range(0,size[0]):

                                Colors.append(img.getpixel((x,y)))
                                Count += 1


                        r, g, b = 0, 0, 0
                        for h in Colors:
                            try:
                                r += h[0]
                                g += h[1]
                                b += h[2]
                            except:
                                pass

                        r, g, b = r/Count, g/Count, b/Count

                        BlockColors.append([i,[r,g,b]])

                        break


        img = Image.open(imgpath)

        if not scale == 1:
            x, y = img.size[0]*scale, img.size[1]*scale

            x, y = int(round(x,0)), int(round(y, 0))

            img = img.resize((x, y))

        size = img.size

        newcommands = ""

        for x in range(0,size[0]):
            rowcommand = ""
            #x = size[0]-x-1
            for y in range(0,size[1]):
                #y = size[1]-y-1
                #p2 = [x,y]

                pixel = img.getpixel((x,y))





                nearest = 255*10
                currentobject = []

                for a in BlockColors:
                    Color = a[1]
                    r, g, b = Color[0] - pixel[0], Color[1] - pixel[1], Color[2] - pixel[2]

                    if r < 0:
                        r = r*-1

                    if g < 0:
                        g = g*-1

                    if b < 0:
                        b = b*-1

                    distance = r + g + b

                    if distance < nearest:
                        currentobject = a[0]
                        nearest = distance

                    if direction == "x":

                        p = [size[0] - x + blockposition[0],size[1] + blockposition[1] - y, blockposition[2]]

                    elif direction == "z":

                        p = [blockposition[0],size[1] + blockposition[1] - y, size[0] - x + blockposition[2]]

                    elif direction == "y":
                        p = [size[0] - x + blockposition[0], blockposition[1], size[1] - y + blockposition[2]]

                try:
                    ppp = pixel[3]

                    if ppp < 200:
                        currentobject = "air"
                except:
                    pass

                if True:
                    if rowcommand == "":
                        rowcommand += "setblock " + str(p[0]) + " " + str(p[1]) + " " + str(p[2]) + " " + currentobject
                    else:
                        rowcommand += "\nsetblock " + str(p[0]) + " " + str(p[1]) + " " + str(p[2]) + " " + currentobject



                if p[1] > 255:
                    raise NameError("Cant place Blocks: Max height reached")
            if not Fast:
                self.run(rowcommand)
            else:
                newcommands += rowcommand + "\n"

        if Fast:
            self.run(newcommands)
