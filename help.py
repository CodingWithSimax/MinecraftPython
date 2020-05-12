import minecraft


WorldPath = r"C:\Users\simon\AppData\Roaming\.minecraft\saves\PythonTestWorld"      #path to your Minecraft World
datapackName = "PythonTest"                                                         #Defining the Name of the Datpack (You can be creative!)

cmd = minecraft.cmd(WorldPath, datapackName)                                        #Setting up World (If you do this the first Time for the World, you need to leave and join your World)

#--- run Commands
cmd.sayInChat("Started")                                                            #say "Started" in Chat

cmd.run("say hi")                                                                   #run command

#--- get Chat-Output
NewChat = cmd.get_chat()                                                            #get new chat messages in List





#--- Building Image
ImagePath = "Python.png"                                                            #path to your Image (It can be .png or .jpg)
PositionToPlace = (0,110,0)                                                         #Position where to build the picture
BlockTypes = [cmd.types.all]                                                        #Defining Blocks that can be used: You can also only use wool and concrete with "BlockTypes = [cmd.types.wool, cmd.types.concrete]" or: cmd.types.terracotta; cmd.types.planks; cmd.types.materials     For All Types: cmd.types.all
TexturePath = r"C:\Users\simon\AppData\Roaming\.minecraft\resourcepacks\PureBDcraft  64x MC115"     #set Path to unzipped texturepack. Without a Texturepack the programm wouldnt know which Block has which color
ImageScale = 0.1                                                                    #Defining the Scale of the Image
Axis = "y"                                                                          #Defining the axis to draw the image. You can use: x, y or z

cmd.build_image(ImagePath, PositionToPlace, BlockTypes, TexturePath, ImageScale, Axis)              #Building the Image. You dont need to set the ImageScale or Axis. Default of ImageScale: 1, Default of Axis: x
