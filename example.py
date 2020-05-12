import minecraft

WorldPath = r"C:\Users\simon\AppData\Roaming\.minecraft\saves\PythonTestWorld"      #path to your Minecraft World
datapackName = "PythonTest"                                                         #Defining the Name of the Datpack (You can be creative!)

cmd = minecraft.cmd(WorldPath, datapackName)                                        #Setting up World (If you do this the first Time for the World, you need to leave and join your World)

#--- run Commands
cmd.sayInChat("Started")

while True:
    Chat = cmd.get_chat()

    for i in Chat:
        if i[1].split(" ")[0] == "!build":
            try:
                Works = False
                try:
                    f = open(i[1].split(" ")[1] + ".png")
                    path = i[1].split(" ")[1] + ".png"
                    Works = True
                except:
                    try:
                        f = open(i[1].split(" ")[1] + ".jpg")
                        path = i[1].split(" ")[1] + ".jpg"
                        Works = True
                    except:
                        cmd.sayInChat("Picture wasnt found.")

                if Works:
                    try:
                        PositionToPlace = (int(i[1].split(" ")[2]), int(i[1].split(" ")[3]), int(i[1].split(" ")[4]))
                    except:
                        Works = False

                if Works:
                    ImagePath = "Python.png"                                                            #path to your Image (It can be .png or .jpg)
                    BlockTypes = [cmd.types.all]                                                        #Defining Blocks that can be used: You can also only use wool and concrete with "BlockTypes = [cmd.types.wool, cmd.types.concrete]" or: cmd.types.terracotta; cmd.types.planks; cmd.types.materials     For All Types: cmd.types.all
                    TexturePath = r"C:\Users\simon\AppData\Roaming\.minecraft\resourcepacks\PureBDcraft  64x MC115"     #set Path to unzipped texturepack. Without a Texturepack the programm wouldnt know which Block has which color
                    ImageScale = 0.15                                                                   #Defining the Scale of the Image
                    Axis = "y"                                                                          #Defining the axis to draw the image. You can use: x, y or z
                    cmd.sayInChat("Building...")
                    cmd.build_image(ImagePath, PositionToPlace, BlockTypes, TexturePath, ImageScale, Axis)              #Building the Image. You dont need to set the ImageScale or Axis. Default of ImageScale: 1, Default of Axis: x

            except:
                pass
